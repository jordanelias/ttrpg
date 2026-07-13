# Mode B — Number System Coherence: Personal Combat

**Target:** `designs/scene/combat_engine_v1/` + shared `params/core.md`.

## Inventory

| System | Range | Scale Basis | Analogous Systems | Inconsistency |
|---|---|---|---|---|
| Attributes (Str/Agi/End/Cog/Att/Spirit/Focus/Rec/Bon/Cha) | 1–7 (`params/core.md:137`) | Bounded TTRPG-style point-buy (31pts/10 attrs, creation max 5, advancement max 7) | Same scale used by every other subsystem (contest, threadwork, mass-battle) | None found — `combatant.py`'s defaults (str=4, agi=4, end=4, cog=3, att=3, spirit=3, focus=3, history=3, disp=4) all sit inside 1–7. |
| History (per-axis) | 0–Recall cap | Point-buy, capped by Recall | Feeds Combat Pool, Fieldwork Pool, Contest Pool identically (`params/core.md:161,253`) | None — Combat Pool's `max(5, History+6)` is structurally the same "History+const, floored" family as Fieldwork Pool's `(Primary×2)+History`, just Agility-independent per ED-901 (a *deliberate* simplification, not drift — see Mode E). |
| Disposition | 1–7, neutral=4, `lean=(disp-4)/3` | Same 1–7 attribute scale, re-purposed as a temperament axis | — | None — `config.py:144-150` documents the neutral-at-4 remapping explicitly and the "both poles cost" design (aggressive risks overcommit, cautious bleeds Vor). |
| Combat Pool | min 5, `max(5,History+6)` | Dice-pool count fed to the continuous roll | Contest Pool / Fieldwork Pool (same construction family) | None. |
| Health | ~13–~50 depending on End/Spirit/Str (see `formula_audit.md` A3.1) | Damage-capacity integer, non-resetting | Composure (social, Cha×3), Thread Fatigue (Spirit×5) — structurally parallel "resource × attribute-weighted formula" family | `params/core.md`'s own printed range/formula is stale (Mode A finding, filed there) — not a genuine scale-inconsistency, a transcription-currency issue. |
| Stamina | 5–35, `(3×End)+(2×Spirit)` (verified: `combatant.py:45-47 stamina_max()`, `systems.py:92-93` thin accessor) | Combat action-economy counter | Concentration (3×Focus+2×Spirit) — same linear-combination shape | None in the code. **But independently found:** `designs/scene/derived_stats_v30.md` §4.2's own "Range" table row states **5–47** (Spirit/End 1–7) directly beneath its own "Formula" row stating `(3×End)+(2×Spirit)` — those two rows of the *same* table disagree (3×7+2×7=35, not 47; even the pre-ratification formula it says it replaces, `Endurance×5`, tops out at 35, not 47). Internal to `derived_stats_v30.md` itself, not a code bug — the live `combatant.py` implements 35 correctly (verified `stamina_max(7,7)==35` by hand). Filed in gap register as GAP-PC-7 (P3). |
| Concentration | 5–35, `(3×Focus)+(2×Spirit)` | Attention/composure resource | Stamina (see above) | None. |
| net_sigma / commit / initiative / poise (engine-internal continuous quantities) | Unbounded-but-soft-capped (`net_sigma`), continuous 2–5 (`commit`, via `2+3×Beta(a,b)`), ±1.5 hard-capped (`initiative`, `INIT_CAP`), 0.5–1.0 (`poise`, `POISE_FLOOR`) | Physics/sigma-derived continuous scales, each with its own anchor constant (`REC_I_REF`, `LEVER_REF`, `PERC_AUTH_REF`, etc.) rather than a shared 1–7/1–10 band | No direct analogue elsewhere in the corpus — these are engine-internal only, never surfaced as a player-facing stat | **Not a defect.** This is a deliberate, Jordan-ratified departure (`combat_balancing_methodology.md §1`: "the ratified dice distribution is the smooth continuous engine... VFIVE board-game sampling was rejected for the videogame") — the videogame combat layer runs on physics-grounded continuous units, while the board-game/TTRPG layer (`params/board_game.md`) presumably stays on discrete/bounded scales. Flag as a **structural observation**, not a coherence bug: anyone unifying `params/*.md` number systems (CLAUDE.md §5's "recommended, not yet built" typed engine-params layer) needs to know these two families (bounded-attribute vs. continuous-physics) will never collapse onto one scale by design. |
| Weapon morphology primitives (`mass` kg, `head_len`/`grip_len` metres, `pommel_kg`) | Real physical units (metres/kg) since the 2026-07-05 U0 units-honesty pass (ED-PC-0002) | SI units, replacing the prior length-unit (`lu`) abstraction | — | None — this is itself a *resolved* prior Mode B issue (U0 explicitly retired the ambiguous `lu` scale in favour of honest metres; `config.py` comments document every rescaled constant with its old→new conversion factor). Confirms the corpus actively self-corrects this category of finding. |

## Redundant-lever check

No redundant difficulty-lever pair (the TN×Ob double-dip pattern Mode B watches for) was found: `TN`
is a fixed constant (`SL.TN_STANDARD`) and `Ob` is fixed at `DECISIVE_OB=3` for every personal-combat
roll — all differentiation happens through `net_sigma` (pool stays a single, unmodified lever). This
is architecturally simpler than the classic TN×Ob interaction and was not flagged as redundant.

## Disposition

No P1/P2 findings in this mode. The one genuine cross-doc numeric mismatch (Health formula) is filed
under Mode A/gap register, not duplicated here. The Stamina range/formula self-inconsistency (above) is
filed as GAP-PC-7 (P3). **No action** — number systems within personal_combat are internally coherent;
the bounded-attribute vs. continuous-physics split is by design.
