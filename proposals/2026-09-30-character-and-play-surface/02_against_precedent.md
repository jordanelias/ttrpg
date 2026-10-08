# Against precedent — scope, concept and emergence, re-scored on the season loop

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: IN (cross-cutting) · IDs: none allocated
## Re-scored at HEAD `c8cc408`. The August verdicts quoted here were judged against the retired campaign driver's campaign, not `engine/season/`.
## Suite: [README](README.md) · [01 the season loop](01_the_season_loop.md) · **02 against precedent** · [03 play surface](03_play_surface.md)

**The question from the session:** if the current plan were finished, how would this game compare with
acclaimed precedent for its scope, concept and emergence? This document answers it on the code as it
stands, re-scoring the repository's own precedent survey against the season loop rather than against
the campaign driver it was written about.

---

## 1. What "the plan finished" means

The plan is `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md` (ED-IN-0281), with its Phase 4
superseded by `workplans/2026-09-30-phase-4-post-ners-revision.md`. Retiring that driver was one
phase of four. Its end-state (§6) consolidates onto the season loop: it deletes
`systems/{overview, factions, world, characters, fieldwork}/`, retires `systems/social_contest/` at
`2-ii`, and keeps `combat`, `mass_battle` and `threadwork`. Phase 2 — governance, settlements, economy,
founding — is in progress and landed much of #444. Faction queries (`20-ii`) are done.

So "finished" means **one engine, consolidated, with governance and settlement content**. It does not
mean faction agency, parliamentary procedure, a relationship model, or a social-contest manoeuvre set;
nothing in the plan builds those.

## 2. Re-scoring the August verdicts

`research/valoria_game_precedent_companion_v1_part3.md` §7.11 (2026-08-28) judged each system against
what the genre treats as table stakes. Re-read against `engine/season/` at `c8cc408`:

| system | August verdict (retired campaign driver) | now |
|---|---|---|
| **faction strategy** | below the floor — a faction was a scalar bundle, one weighted draw a season | **structure without agency.** `faction_q` makes a faction a query over persons, seats and holdings, storing no stat — the parts every surveyed interior presupposes now exist. But nothing acts *as* a faction: `head` is empty and `at_war` false in every buildable world (R-04 partial) |
| **parliament** | below the floor — a vote without procedure | **still below.** `convene`, `petition`, `open_case`, `determine`, `issue` have effects (#444), but `determine` executes zero times on the populated realm; agenda, chair, drafting and recorded defeat are unmodelled; the proceedings subsystem is partly built under plan position `22` (steps 6, 7, 9 and 10 done; the contest-resolution core, steps 11–16, open), while its proposal stays held back |
| **territory and conquest** | below the floor — conquest a colour change | **conquest does not exist.** `march` fights a real field battle; a loss writes casualties, a morale hit and a grudge on the losing side (Jordan's ruling), and the winner gains nothing — no holding changes hands |
| **people** | below the floor — a roster without relationships | **partly moved.** Every person has a private ledger; 37 cohorts eat and migrate. Relationships are `stance` rows `(referent, valence, weight)` read by `choose`, but only `march` writes one |
| **economy** | below the floor — no income anywhere | **a loop without pressure.** MATTER yields stores and cohorts consume them; a shortfall is witnessed and becomes a question to transfer. But no coin exists, no verb produces goods, and the shipped realm runs about 35× surplus, so scarcity rarely bites |
| **settlement governance** | ahead, and unaware — the old tag ledger's residual | the old settlement ledger and its `ledger_sweep` have no counterpart in the season loop; a grudge survives only as a stance row. Offices, conferral and revocation are season-loop verbs, and #444 added terms and upkeep |
| **mass battle — engine** | above the genre | unchanged |
| **mass battle — seam** | below the floor — armies identical but for one integer | **still one real input**: on the season path, troops = summed `Person.weight`, power and morale fixed ([08](08_mass_battle_units.md)) |
| **cross-scale** | at the frontier | at the frontier; R-04 partial. Two modes of one bout ([05](05_two_modes_of_one_bout.md)) are the most concrete route to the personal↔field seam |
| **resolution kernel** | ahead on ownership, behind on calibration | unchanged; σ-leverage contests currently roll with zero leverage ([01](01_the_season_loop.md) §1.2) |
| **social contest** | at the point before Burning Wheel's known failure | unchanged; the manoeuvre set is unauthored |

## 3. Scope, concept, emergence

**Scope.** The nearest whole-game analogue is still Mount & Blade — a character who fights personally,
governs, plays faction politics and fights in mass battles — and the repository defines itself against
it on exactly one axis: Mount & Blade's layers do not couple (part 1 §2.12). Valoria's coupling is the
part at the frontier, and the least built.

**Concept.** Three ideas are genuinely uncommon, and all three are built rather than hoped for:
knowledge that exists only as what each person witnessed or was told, so *a belief can be false and its
holder cannot tell* (the ledger, [09](09_the_character_sheet.md) §1.4); a single resolution kernel shared
by every scale; and a duel resolved from weapon physics and sourced martial technique
([04](04_the_bout.md)).

**Emergence.** The survey's hardest finding applies directly: across Dwarf Fortress, the Nemesis system
and Wildermyth, *tracking* state and *expressing* it proved different problems, and the second is the
one the field failed at (part 2, failure shape D). Valoria tracks well. Whether a decision reaches a
later decision is R-01 and R-02, both **not met** at corpus scale; the last corpus-scale measurement
(stale, per the requirement rows themselves) found about 4 % later-decision divergence against 100 %
world divergence. The narrowest honest statement: knowledge moves — a claim witnessed or told can change
what a later deliberation offers — but disposition barely does. The one attitude a decision now writes
that a later decision reads is a lost march's grudge; apart from it, no act changes how anyone is
inclined toward anyone.

**Verdict.** Ahead where the genre has not settled — the duel, a world without an omniscient narrator,
one kernel for every scale. Below the genre's floor where it settled long ago — factions that act,
procedure, relationships that accumulate, scarcity that bites — with #444 moving economy and factions
from *absent* to *structure without pressure*. Finishing the plan consolidates the engine; it does not
change this verdict, because the missing pieces are not in the plan.

## 4. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **P-1** | Let more acts write relationships, and give every relationship row its cause. `tell`, `give`, `oblige`, `revoke`, `release` are acts another person has reason to remember; each could append a stance row carrying the causing event's id. The survey's strongest synergy (part 2 S1) and its bypassed-chain failure (shape E) both ask for exactly this: small, provenance-bound tags, recombined. | the effects of those verbs; `Person.stance` row shape | R-02's fork-and-follow at corpus scale moves off ~4 %; no stance row lacks a cause | medium | IN |
| **P-2** | Give scarcity teeth, with a reachability bar and a control arm: at default fixtures, shortfalls should occur in ordinary play. A mechanism engineered not to fire is indistinguishable from one that does not exist (part 1 §2.2, EU4's estates). | `SITE_YIELD`, subsistence fixtures | shortfall events per season on the populated realm > 0 at defaults; a control arm at today's yields shows the difference | small | IN |
| **P-3** | Seat faction heads, then let a head act for the faction. The cheapest precedent the survey found is Old World's: goals emitted by a person crossed with the houses around them, expiring on that person's death — it needs the person object and nothing else (part 1 §2.1, part 2 K6). | `faction_q.head`, a `commit` carrying a degree | `head` non-empty on the populated realm; a faction-scale act executes in a season | medium | IN, FA |
| **P-4** | When the proceedings subsystem is taken up, build procedure before the vote: agenda control, the chair's order of motions, and recorded defeat — the last *"nearly free to implement"* (part 1 §2.2). | `proposals/2026-09-05-proceedings-subsystem/` | a carried-and-vetoed motion persists as a citable record | small–medium | SC, when un-held |
| **P-5** | Point the August verdict table at this re-score, so the next reader does not take the retired driver's verdicts as the season loop's. | one line in `research/valoria_game_precedent_companion_v1_part3.md` §7.11 | — | trivial | IN |

No new Jordan item: the order in which these are taken up is the plan's to set.
