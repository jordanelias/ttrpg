# CHAR — the character's side of the capability surface: what a definition says to a reader, levels, bundles at a rank, and the cast row's unread keys

Reconciled: 2026-11-12, U5a closure (`unified/U5_CONFLICTS_U5a.md` C-U5a-08) — the table this file would not name a path for is `references/descriptor_registry.yaml: capabilities` (`unified/U1_CAPABILITY_AUTHORING_ARCHITECTURE.md` §1–§2); `gloss` is a required field of that block.

## Status: PROPOSED

Written by the CHAR audit lane, addendum B (`audits/02_CHAR_audit_addendum_B.md`, §B4, F-CHAR-16,
F-CHAR-19, F-CHAR-21; B6.2 rows 4 to 6, 13, 14, 18, 22, 24). Ratifies nothing. Reference under
`CLAUDE.md` §0.05. **It adds to, and does not restate,** `10_DICE_capability_axiom_map.md` (the ten
roles, the definition row, the uses table) and `01_CORE_capability_authoring_surface.md` (the same
row, the verb column, the cast row's `capabilities:`). Where those two differ on the file that holds
the definition, this proposal takes no side: every edit below names the table, not the path.

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

Every row of the capability definition table carries `gloss:`, one sentence in plain words saying
what the capability is. The loader refuses a row without one, as the verb loader refuses a missing
`beneficiary:`. The ten attributes gain the same key where they are defined
(`references/descriptor_registry.yaml: attributes`); three of them (Focus, Reason, Presence) carry no
description today (`rosters.yaml:1588`). Readers: `decision/sheet.py` gains
`describe(key) -> str` (the leaf's text, no `World`); the first lane's reason trail prints it beside
a capability use that fired. The four existing rows, for Jordan to correct:

| id | proposed `gloss` |
|---|---|
| `copying` | Carries a text or a message on exactly as it was given. |
| `argue` | Makes a case to someone's face and moves them by it. |
| `inquiry` | Finds things out: from a record, a place or a watched person. |
| `arms` | Fights with a weapon in hand. |

### Edit 2 · `rank_at_least` as a `when` key (step 4: the map's `when` roster)

One more member of the uses table's closed `when` keys: `rank_at_least: <n>` holds when the holder's
rank in the row's `key` is at least `n`. It is how a skill's higher level changes *what* it does: two
rows on one key, the second under `rank_at_least: 3`. One comparison in the uses reader; no row
ships.

### Edit 3 · a bundle may grant at a rank (step 4: CORE's edits 5 and 9)

In `tables.lifepath_templates`, an entry of `holds:` may be `{<id>: <rank>}` as well as a bare id; a
bare id keeps today's meaning (the untrained value). The loader checks the rank against the
capability's `scale`. No rank is authored here: which lifepath starts a person at what is content,
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
are one change to one dataclass.

### Edit 6 · three register rows (step 1)

`engine/season/hole_register.yaml`, text only: H-46's last sentence (*"`rosters.yaml` still carries
the OLD thirteen"*) is struck with the date; H-148's `hole:` opens with the CR-24 state it now
describes in a bracket; H-170's cite gains one line that `body_step` reads 10 today and its readings
were taken at 0.

## What a definition must carry, in one place

The full field list by kind (skill, ability, aptitude, trait), with the tradition's word for each and
its reader, is the table in the addendum's §B4 (c). In short: the map's six fields, plus `gloss`; a
use row per effect, with `when` (now including `rank_at_least`); and nothing about loss, because a
capability is never lost. An *ability* is not a fifth kind: it is a trait or aptitude whose use row
names its scene's site, and a combat ability waits on the combat module exporting its lever roster.

## The gate (an execution artifact)

(a) The NPC-088 headless hash and `build_realm(0)`'s build hash, EQUAL before and after. (b) A
definition row with no `gloss`, and a cast row with an unlisted key, each refuse at load with a
message naming the row. (c) `describe("inquiry")` returns the sentence; a `DevelopmentSheet` for
`p_npc_001` shows Thread Sensitivity 75. (d) With a test row `{…, when: {rank_at_least: 3}}`, a
holder at rank 2 and one at rank 3 read different levels from the generic advantage source.

## The falsifier

Any hash in (a) moves (an edit that was to change nothing changed something). Or, after edit 4, a
search finds a reader of a deleted key (it was not unread). Or (d)'s two holders read alike.

## NERS reading (`CLAUDE.md` §0.06; E last)

- **N.** From the designer's side a capability he cannot describe on the row he defines is a number;
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
