# Character and play surface — a digest of one design session

## Status: PROPOSED (2026-09-30) · design-only · **HELD BACK IN FULL: merging this directory ratifies nothing** (`CLAUDE.md` §2's default is waived here, loudly) · reference under `CLAUDE.md` §0.05
## Lanes: IN, PC, MB, SC, FI · IDs: none allocated · `references/id_reservations.yaml` untouched
## Measured at HEAD `c8cc408` (#444). Every figure was produced by running the named function or harness; an independent read-only critic attacked the drafts against the tree.

**What this is.** One session's questions about Valoria — how the season loop runs, how the game stands
against its precedents, what an interface could play, the bout and its two proposed modes, weapons and
armour, mass-battle units, the character sheet, and the verbs' demands on attributes — digested into ten
documents. Each pairs an analysis with recommendations, and each recommendation carries its falsifier.

**What it changes in `engine/season/`** (`CLAUDE.md` §3 asks this of any new directory here): nothing
directly. The recommendations that would touch it, if taken up, are S-1, S-2 and L-1 (a client's read
and write boundary), M-1 (return the fight trace), K-2, K-3 and K-4 (the person's fields and a writer
for capability), P-1, P-2 and P-3 (relationships, scarcity, faction heads), V-1 (a verb-table row) and
U-1 (musters). The rest touch `systems/` or are standing rules.

---

## Reading order

| | document | answers |
|---|---|---|
| **the game** | [01 the season loop](01_the_season_loop.md) | how one season runs; why seeded contests reproduce; where the requirements stand |
| | [02 against precedent](02_against_precedent.md) | how the game compares with acclaimed precedent, re-scored on the season loop |
| | [03 play surface](03_play_surface.md) | what an interface could bind to; which subsystem is nearest to playable |
| **the bout** | [04 the bout](04_the_bout.md) | the personal combat engine, martial traditions, the nine moments |
| | [05 two modes of one bout](05_two_modes_of_one_bout.md) | a grid mode and a duel mode over the same engine |
| | [06 weapons from physics](06_weapons_from_physics.md) | how a weapon's parts become its behaviour; where armour enters; five findings from running it |
| | [07 saying a weapon is good](07_saying_a_weapon_is_good.md) | how a player can tell a good weapon from a bad one without being handed a fixed number |
| **the field** | [08 mass battle units](08_mass_battle_units.md) | what kinds of unit the engine allows, and how units should be composed |
| **the person** | [09 the character sheet](09_the_character_sheet.md) | what a person is in code; one sheet reconciled across subsystems |
| | [10 verbs and attributes](10_verbs_and_attributes.md) | which verbs have work for an attribute, read four ways including etymology |

---

## Recommendations, ranked

Ranked by what each unblocks, then by cost. Ids resolve to the rows in each document.

**First — buildable now, small, and each unblocks others**

1. **S-1** a dispatching `choose` — the whole single-player hook; its control is a hash comparison.
2. **M-1 / S-4** return the combat trace the seam already captures — needed by B-3 and by any grid
   display.
3. **S-2** a per-person projection as the only thing a client reads — the epistemic contract in code.
4. **B-3** measure tradition identity per event at the nine moments — it gates B-1 and M-4.
5. **K-2** an unseeded `attributes` dict on `Person` — it unblocks K-1, K-6 and U-4 without pre-empting
   the roster.
6. **K-3** the two licensed practitioner fields, and a typed `thread_read` — the sixth inquiry becomes
   attemptable.

**Second — medium, and they change what the game is**

7. **P-1** more acts write stance rows, each carrying its cause — the emergence gap (R-01, R-02).
8. **P-3** seat faction heads and let a head act — factions from structure to agency.
9. **P-2** give scarcity teeth, with a control arm.
10. **K-1** build the `Combatant` from the person — a character's build reaches their fights.
11. **K-4** a `practice` verb as capability's writer — heeding 10 §2.3: the chooser must see what was
    acquired.
12. **U-2, then U-1** one equipment model for both scales; musters with inputs beyond headcount.
13. **L-3** name the zero-leverage state, and choose a producer for σ-leverage advantage.
14. **M-2, M-3, M-5** the duel and grid cadences, after the two items below are ruled.

**Repairs — trivial, any time:** L-2, B-2, W-4, P-5, and V-5's gloss; W-3 puts the recovery tail on
the balance harness.

**Ordered behind other work:** C-1, the weapon card, is buildable now, but C-2's words wait on W-1,
W-2 and W-3 (C-4, C-5); B-1 → M-4 (the Plan layer's own precondition); U-4 and K-6 after K-2; L-4 is
the plan's.

**Held with the proceedings design:** P-4, V-4, and V-5's speech-kind name.

**Standing rules:** S-7, B-4, K-7, V-2, C-3.

---

## For Jordan

Three items survive `CLAUDE.md` §0's five tests:

1. **05 §4.1** — do fights nobody watches resolve inside one act, or span scenes as a grid fight does?
2. **05 §4.2** — does duel mode open any of the three closed moments? Recommended: no.
3. **10 V-1** — split `evade / defy` into two rows; it amends a ratified §E3 row.

Already his, and not re-opened here: the attribute roster (OPT-AV-1; the plan's D2), Focus and
Charisma (the August proposal), and the Godot version. 08 records where a levy/professional `Muster`
split would sit if pursued; it is not proposed.

---

## What the session said that this suite corrects

The session's answers were given in conversation; writing them down against the tree changed these.
The documents carry the corrected figures.

| said in session | measured |
|---|---|
| rapier parry affinity 0.93 | **0.70**. The literals are stale; the baked guards (hand 0.68, blade 0.54) overwrite them — 06, 07 |
| *shinogi* is German, and effectively katana-only | Japanese; the spine lever reaches **25** single-edged weapons — 06 |
| *ringen am Schwert* needs a half-sword weapon | it reads the **opponent's** `grab_hazard` — 06 |
| the poleaxe switches to its hammer at plate | the poleaxe punctures at every tier; the **bec de corbin** switches to percussion at heavy — 06 |
| a badly balanced sword parries and winds worse | those affinities move by hundredths; the penalty is in recoverability (×2.2) and tempo, and because `material` has no reader a blunt copy clears heavy plate whether it is wood or steel — 06, 07 |
| seven of twelve levers carry abilities | seven of **fifteen** — 04 |
| standing does not exist in code | `standing_of` exists and measures a perception gap; no 0–7 rank exists — 09 |
| capability's one writer zeroes it | the corpus cast writes authored values; a probe zeroes it — 09 |
| R-04 not met; faction queries blocked | R-04 **partial**; `20-ii` **done** — 01, 02 |
| 42 verbs; social 14, material 10, movement 1 | **44**; social 15, material 13, movement 2 — 10 |
| `examine` and `surveil` are contested because they are exposed | the stratum is an ordering band over what an act touches — 10 |
| attributes for seat, bond and decree verbs | none of them contests, and §E4 forbids a modifier on them — 10 |
| `confer` is consultative | it bestows a seat — 10 |
| 22 `_emit` sites; nothing in the seam sets `_TRACE` | **20** sites; the seam captures the trace and keeps only `bouts` — 04, 05 |
| fieldwork's sim is stubs | only `knots.py` remains, uncalled by the season loop — 03 |
| `refract` | renamed **`construe`** (Jordan, 2026-09-18) — 10 |
| eleven troop types have presets | **ten**; `mounted_archers` has none — 08 |

Comparisons with other games are marked `[UNVERIFIED]` where they rest on recall rather than on the
repository's own precedent survey.
