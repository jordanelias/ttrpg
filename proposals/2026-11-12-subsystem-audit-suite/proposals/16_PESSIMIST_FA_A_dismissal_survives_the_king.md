# PES-FA-A — the power to dismiss survives the King, reaches a duke's own council, and can be undone

Reconciled: 2026-11-12, U5d closure — folded **A-19**, **A-37** and **A-58**. Edit 1's `successions: off_duke_valorsmark: off_heir` is written in the set-of-titles shape (`22_HAPPENINGS_B` edit 2) and the duchy passes to whoever takes the throne in the race, not to the heir by right; the claim is a draw. Edit 3 (a dismissing seat can pardon) stands and agrees with A-37 (an imposed bar ends by the bench's pardon or its term, never by the barred man's own release). Edit 2 anchors six council seats on a territory: under A-58 a seat goes with the land it is anchored on, so those six seats pass to the seizer when a victor standing on that territory chooses to seize it (A-66; an occupier who does not seize leaves them with their holders); the author's choice of territory is therefore also the choice of what a conquest of it carries, and this is stated at the rows.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §2 and U3 C3-K9 (A-19: edit 1 written in
`22_HAPPENINGS_B` edit 2's set-of-titles shape; lands after it), §2 (A-58: one line per re-anchored row on what a
seizure carries), §7/§7b (territories, tests replacing the `pf*` probes, tier); U3 B21, C3-D5 (order inside B21), C3-L7
(seats pass with land only through `revocation: holder_of_rung`). **Corrections at the tree.** (1) The two seat
territories are decidable from a file the build reads: `systems/settlements/valoria_geography_v30.yaml` places
Hafenmark's constitutional capital, Gransol (S-018, "Baralta's court"), in `T8`, and Varfell's ducal capital,
Sigurdshelm (S-031, `type: Seat`), in `T12`; R5 7b's `[ASSUMPTION]` `terr_T7` / `terr_T4` (lowest-numbered child) is
replaced. (2) The U5d head line above says the six re-anchored seats pass to a seizer of the territory; under C3-L7 a seat
passes with land only if its row carries `revocation: holder_of_rung`, and these six keep `rung_above_same_faction`
(the ruled ED-IN-0256 (3) basis this edit brings them under), so they pass with the ducal seat, not with the territory
alone; the per-row line says so. (3) `22_HAPPENINGS_B` edit 2 names this file's row as `off_duke_valorsmark: [off_heir]`,
which is the "heir by right" reading the U5d head refuses under A-19; this file writes the throne's title set (for
another lane: HAP_B's parenthetical).

## Status: PROPOSED

Lands in batch: **B21** (FA). Depends on: `22_HAPPENINGS_B_the_throne_is_never_stranded.md` edits 1-2 (B21, the
set-of-titles shape; lands first, C3-K9), `06_FA_seat_terms_and_turnover.md`, `06_FA_decree_binds.md`,
`14_VERBS_BINDING_C_turnover.md` (B21; inside the batch this file follows BIND_C's flip and precedes
`14_VERBS_BINDING_D`, C3-D5).

Source: `audits/16_PESSIMIST_FA.md` F-PES-FA-02 (premise P5; runs `pf1_static.py`, `pf2_premise.py` P2 and
P5, `pf2b_followup.py` §1 and §4, seed 0). Binds on, and does not redo: CP-T09-06 (the Duchy of Valorsmark's
basis), `06_FA_seat_terms_and_turnover.md` edit 6 (a ban's scope), `14_VERBS_BINDING_C_turnover.md` (`revoke`
and `pardon` become draws; this file changes who may attempt them, never the outcome),
`06_FA_decree_binds.md` (the recall occasion, which needs a seat that can recall).

## What it changes in `engine/season/` at runtime

1. After a King dies and his heir claims, the heir holds the Duchy of Valorsmark as well as the throne, so
   the six Crown seats that can be stripped today can still be stripped. Today they cannot: the claim opens
   one seat of the two and the realm is left with no seat able to dismiss anyone.
2. The Duchess of Hafenmark and the Duke of Varfell can strip the seats of their own councils: six of the
   seven seats that declare `rung_above_same_faction` and that nobody can strip today. The seventh, the
   Guild Comptroller, resolves to the faction `Guilds`, which has no seat above it; it stays strippable by
   nobody and this file says so instead of pretending otherwise.
3. A seat that can dismiss can also pardon the ban its dismissal opened. Today no seat in the realm can do
   both, and `pardon` of a dismissed man is refused through every one of the 33 held seats.

No hash moves at build. Edits 1 and 2 are data; edit 3 is data. None adds a field, a kind or a predicate.

## The problem (evidence, by execution)

- **Six of 34 seats can be stripped, all six through one seat, `off_duke_valorsmark`, and none through
  `off_king`** (`pf1`, grant-filtered): the rule is the seat on the rung *directly* above
  (`state/gate.py:485-507`, pinned by `test_13d_i_an_empty_parent_refuses_even_a_same_faction_grandparent`);
  the Crown's officers sit on `terr_T1`, whose parent is `duchy_valorsmark`, and the realm is two rungs up.
  The King's `revoke` of the Royal Marshal through `off_king`: `revoke.refused`; through
  `off_duke_valorsmark`: `tenure.closed`.
- **`off_duke_valorsmark` declares `conferral: null`**, so once empty it is filled by nothing
  (`gate.py:697-698`, `has_filler` false). The King dies, the heir claims (`succession.claimed`):
  `off_king` is his, `off_duke_valorsmark` is empty, his own `confer` of it on himself is
  `confer.refused`, and **the set of strippable seats in the realm is empty**; his dismissal of the Marshal:
  `revoke.refused` (`pf2` B2). `_eff_succeed`'s docstring says "the King who dies holding two such seats
  leaves both to one claim" (`effects_governance.py:148-150`); `successions` has one row.
- **Seven seats declare `revocation: rung_above_same_faction` and can be stripped by nobody**: Hafenmark's
  Legal Advisor, Military Commander, Commune Representative and Guild Comptroller, and Varfell's Senior
  Jarl, Skald-Chief and Military Jarl. Each is anchored on its duchy's own rung, the rung its duke's seat
  is on, so no seat is on the rung above it in its faction. The Crown's equivalent officers are anchored
  one rung down (`terr_T1`), which is the only reason the rule reaches them.
- **A dismissal's ban cannot be lifted.** `_eff_revoke` opens `ban : him -> Act.via`; `pardon` is
  `remit:determine` exercised through the ban's object seat (`verb_table.yaml`, `pardon`;
  `effects_governance.py:368-396`). `off_duke_valorsmark` grants `confer, convene, issue, revoke`. `pardon`
  of the dismissed Marshal tried through all 33 held seats: 33 `pardon.refused` (`pf2b` §4). The seats
  whose rows grant both `revoke` and `determine` are `off_king`, `off_widow_regent` and `off_confessor`,
  and none of the three can strip anything. The ban bars every seat of every faction (`pf2` C1b: the Duke
  of Varfell's `confer` of an elected Varfell seat on him is refused; control, the same seat to the Clerk
  opens).

## The resolution, decided

| # | decision | ladder step |
|---|---|---|
| 1 | The Duchy of Valorsmark passes with the throne: `conferral: inheritance` (CP-T09-06's edit, corrected by the FA lane's R-18 to `null → inheritance`) **and** a `successions` row to the same title. CP-T09-06 as carded changes the basis and names no row; without the row `check_successions` refuses the load, and with it the docstring's "leaves both to one claim" becomes true | 3 (the effect's own docstring), 1 (CP-T09-06) |
| 2 | Six of the seven council seats (all but the Guild Comptroller, whose faction is the Guilds) are anchored one rung below their duchy, on the territory of the ducal seat, as the Crown's are on `terr_T1`. The ruled basis ("rung above of same faction", ED-IN-0256 (3)) is not touched; the data is brought under it | 4 (the Crown rows' precedent) |
| 3 | Each of the three ducal rows gains `determine`. A duke holds a bench in his duchy; the hand that dismissed can reinstate. The alternative, a second eligibility on `pardon` (`remit:revoke`), would need a second basis beside `bench` in the gate for one case, which is more apparatus for the same play | 4 (`off_king`'s row carries both), 5 |

Not decided here, and named: the King as King still dismisses nobody (the realm is never the rung directly
above a seat that is not a duchy seat). That is the ruled rule working as ruled; a King who wants a duke's
officer gone must go through the duke, or through a court. The audit's §5 records it as accepted and not
re-raised, with its measured consequence (a King with appointment at every depth and dismissal at none).

## Exact edits

1. **`engine/season/offices.yaml`, row `off_duke_valorsmark`**: `conferral: null` → `conferral: inheritance`.
   **`engine/season/rosters.yaml: successions`** (the `{seat: [title, …]}` shape of `22_HAPPENINGS_B` edit 2,
   which lands first): add `off_duke_valorsmark` with **the same title list as `off_king`**
   (`[off_heir, off_widow_regent, off_princess, off_duchess_hafenmark, off_duke_varfell]` as HAP_B edit 2
   writes it), so whoever takes the throne in the deed race (A-19) takes the duchy with it: a list is
   eligibility, the claim is the draw. (`claimable_seats` already returns every vacant seat whose title is the
   claimant's; `_eff_succeed` already opens all of them in one write. No code edit.)
2. **`engine/season/offices.yaml`**, the `rung:` anchor of six rows: `off_legal_advisor_hm`,
   `off_military_commander_hm`, `off_commune_rep_hm` from `{duchy: "Hafenmark"}`
   to `{territory: "terr_T8"}` (`off_guild_comptroller` is left where it is: its
   faction is `Guilds`, so no anchor brings it under the Duchess); `off_senior_jarl_west`, `off_skald_chief`,
   `off_military_jarl` from `{duchy: "Varfell"}` to `{territory: "terr_T12"}`. The territories are read from
   `systems/settlements/valoria_geography_v30.yaml`: `T8` holds Gransol (S-018), *"Hafenmark constitutional
   capital. Baralta's court"*; `T12` holds Sigurdshelm (S-031, `type: Seat`), Varfell's ducal capital (the
   roads list names it so). Both are among the children listed at `build_realm(0)` (Hafenmark `terr_T7`,
   `terr_T8`, `terr_T10`, `terr_T17`; Varfell `terr_T4`, `terr_T11`, `terr_T12`, `terr_T13`). The Crown's
   officers sit on `terr_T1`, Valorsplatz's territory, the realm's other `type: Seat` settlement: the same
   precedent. If the Senior Jarl **of the Western Highlands** is meant to sit on his own highland territory
   rather than at the ducal seat, his row takes that territory; the rule reaches him either way.
   Each of the six rows gains one comment line (A-58, C3-L7): *"anchored on `terr_T8` (`terr_T12`): its
   `revocation:` is `rung_above_same_faction`, not `holder_of_rung`, so a seizure of this territory alone does
   not carry this seat; it passes with the ducal seat"*.
3. **`engine/season/offices.yaml`**, rows `off_duke_valorsmark`, `off_duchess_hafenmark`,
   `off_duke_varfell`: add `determine` to `remit_acts`.

`remit_acts` edits re-stamp nothing at build (the grant is stamped when the hold opens). `offices.yaml`'s
header counts and `engine/engine_params/` exports that carry the rows are re-derived with the repo's own
exporter (`--check`), not by hand.

## Gate (execution artifacts)

`pf1_static.py`, `pf2_premise.py`, `pf2b_followup.py` and `pf6_fixcheck.py` were lane scratch, not in the
repository (U3 §6.2). Their equivalents are written first as NEW `engine/season/tests/test_fa_dismissal.py`:
`test_strippable_set_at_build_includes_six_council_seats` (G1, with the `off_king` and Guild Comptroller
controls), `test_heir_holds_both_titles_after_one_succeed` (G2), `test_dismiss_then_pardon_through_the_ducal_seat`
(G3), `test_pardon_through_off_king_still_refused` (G3's control). Command:
`python -m pytest engine/season/tests/test_fa_dismissal.py engine/season/tests/test_in31_revocation_cost.py engine/season/tests/test_in61_succession.py engine/season/tests/test_in12_arrest.py engine/season/tests/test_g3_not_yours.py -q`
(the last four exist). Readings:

- **G1** `strippable(w)` at build is a superset of today's six and includes six council seats, each
  through its duke's seat. Control: `off_king` strips none of the twelve (the rule is unchanged), and the
  Guild Comptroller is still strippable by nobody.
- **G2** after the King's death and the heir's one `succeed`: `off_king` and `off_duke_valorsmark` are
  both held by the heir; `strippable(w)` equals its value at build; the new King's `revoke` of the Marshal
  through `off_duke_valorsmark` closes the hold. Today: empty set, `revoke.refused`.
- **G3** the King dismisses the Marshal through `off_duke_valorsmark`, then `pardon`s him through the same
  seat: `ban.ended`; the reappointment then opens. Control: `pardon` through `off_king` (not the ban's
  object) is still refused. Today: 33 of 33 refused.
- **G4** at the close, the files covering what the edits touch: `engine/season/tests/test_in31_revocation_cost.py`,
  `test_in61_succession.py`, `test_in12_arrest.py` (the `pardon` cases) and `test_g3_not_yours.py`.

## Falsifier, and its outcome with the edits applied in memory

Each edit was applied to a forked world in memory (no file written) and its gate run: `pf6_fixcheck.py`,
seed 0, output `runs/PES_FA/pf6.txt`.

- G2 would fail if a second seat under one title were treated differently from the first. **Observed:**
  with the basis and the row, the heir's one `succeed` gives him `off_king` and `off_duke_valorsmark`; the
  strippable set is the same six seats before the death and after the claim; his `revoke` of the Marshal
  through the ducal seat: `tenure.closed`. (The import-time `check_successions` was not re-run against
  edited files; it reads `offices.yaml` and the roster at load `[UNVERIFIED]`.)
- G1 would fail if a council's body resolved to a faction other than its duke's. **Observed:** re-anchored
  on a territory of the duchy, `off_military_jarl`, `off_skald_chief` and `off_legal_advisor_hm` pass
  `may_revoke` through their duke's seat (false before), and the Duke of Varfell's `revoke` of the Military
  Jarl closes the hold with no ban (an elected seat). **`off_guild_comptroller` does not pass**: its
  faction resolves to `Guilds`. That is the one the first draft of this file got wrong, and why the edit
  now names six rows.
- G3 would fail if the bench asked more than the grant and the object. **Observed:** with `determine` on
  the ducal seat's grant: dismiss `tenure.closed`; pardon through the same seat `ban.ended`; reappoint
  `tenure.opened`; control, pardon through `off_king`: `pardon.refused`.

## NERS reading (definitions `CLAUDE.md` §0.06; E last)

- **N.** Top-down: a ruler who cannot remove an officer has no instrument but appointment into vacancies,
  and there are none. Bottom-up: an officer who cannot be removed has nothing to fear from failing.
  Lateral: the FA lane's recall occasion (`06_FA_decree_binds.md`) and VB-C's contested `revoke` both end
  in an act that, after one royal death, no seat may attempt. Diagonal: Hafenmark and Varfell get the
  same instrument the Crown has. Cut it and what dies is every fall from office in the game.
- **R.** The half with no player: dismissal, ban, pardon and reinstatement become a four-beat story any
  duchy can produce. Extremes: the royal line's second title no longer strands the realm; a top-rung seat
  remains strippable by nobody, as ruled.
- **S.** One rule (the rung directly above, same faction) now gives the same answer in all three
  duchies. `pardon` stays one methodology (`bench`).
- **E, against that.** Three data edits and no code: the overhead is one more remit act on three rows. The
  player can now intuit "my liege can remove me, and can take me back".

## Cost class

Edit (data). Dependency: HAP_B edit 2's shape (above); VB-C makes the outcomes draws. Hash movers declared: none
at build (the falsifier ran in memory); the `offices.yaml` header counts and exports re-derived by their exporter's
`--check`. Tier: `sonnet`, effort `high`. Lands it: B21, one commit per edit (1 after HAP_B edit 2; 2; 3), then the
test file.
