# ERAS, REGIMES, STRIFE AND MOMENTUM — audit, design and plan

## Status: REFERENCE (an audit and a plan; resolves nothing at runtime, CLAUDE.md §0.05)
## Read at: 2600cb0 (working tree)
## Lane: WR (with GO for the player-facing part), under the standing charge at the end of `AUDIT_BRIEF.md`

Charge (Jordan, 2026-11-12): *"have Fable extend author and plan how to improve upon eras regimes and strife alongside methods to make the plot legible to player. work to improve era endings (like death of monarch, change of rule, civil war breaks out, etc) and momentum mechanisms. cascade effects and compounding are real"*.

Proposals carried by this audit (each with its coding instructions, per the brief's last standing charge):

| file | what it decides |
|---|---|
| `proposals/30_WR_A_the_era_is_a_named_period.md` | the era as a named reading with a kind, a bearer and a successor; the era endings |
| `proposals/30_WR_B_regimes_who_believes_whom.md` | the regime as a reading over held affiliations and seats: forming, merging, splitting, ending |
| `proposals/30_WR_C_strands_open_grow_join_conclude.md` | the strand life cycle, several at once, the ending that fails to come |
| `proposals/30_WR_D_momentum_and_its_brakes.md` | compounding by drawn acts on person-side readings, and the brakes |
| `proposals/30_WR_E_cascade_chains_and_the_census.md` | the cascade chains for the stories and happenings; census gates and controls |
| `proposals/30_GO_F_the_plot_as_the_player_is_shown_it.md` | the player's marker, strands as named stories, news, slate, recap, foreshadowing, end reveal, the reason trail |

## 0. Verdict

**Not yet a sound basis, and the obstacle is one of kind, not of quantity: the engine has strife and calls its realm-wide scope an era, but it has no era in the sense the charge asks for (a named period that ends when a monarch dies, the rule changes or a civil war breaks out), no regime beyond a pairwise credit factor, no momentum that is a person's rather than a count's, and nothing of any of it reaches a player.** What exists is good ground and should be kept whole: `queries/world_q.py::flows_in` (`:5172`) reads strands and eras from the Event log and stores nothing; `flows_known` (`:5473`) reads a person's own strands from his ledger; `flow_stakes` (`:5524`) stamps what is at stake onto his questions, shipped on (`data/fixtures.py:1024`); `commensurate` (`:5317`) and `loop/witness.py::_credit` (`:240`) grade a told claim by whether teller and hearer hold compatible affiliations, shipped at 0.5 (`data/fixtures.py:1086`). Every one of those is a reading or a factor on belief; none fires anything, which is what `ED-IN-0225` and the strife master's T-a/T-b require and what this plan keeps.

Three things are missing, in order of weight. (1) **The engine's `Era` is a scope with no content**: it opens on the first strife move in the realm and closes on a realm-rung terminal move with no open referent (`world_q.py:5233-5252`); it has an id and a move list, and no kind, no bearer, no name and no successor, so "the reign of Almud ended and the interregnum began" cannot be said by any reader; a monarch's death is a `joins` kind (`rosters.yaml:3390`) and natural death is off (`data/fixtures.py:690-691`), so the commonest era ending in the tree's own history cannot occur in default play. (2) **Compounding is unmeasured and unbounded by design rather than by reading**: the loops L1 to L4 are declared with asserted signs (`strife-00` §6), the guard reads terminal-code shares, and nothing distinguishes a chain that compounds (the first act raised the odds of the second) from one that merely co-occurs. (3) **The player is shown none of it**: the chronicle renders one deepest cause chain for an outside observer (`harness/chronicle.py`), the person reading holds "no era object" (`world_q.py:5379`), and the player-surface contract (`proposals/11_GO_player_surface_contract*.md`) carries no era marker, no strand list and no recap.

The plan below adds no stored era, no counter, no trigger and no era-level draw. An era ends because a person's drawn act, or the world's drawn motion, changed the state the era reading reads; the reading then names what ended and what began. One ruling is touched at one point (§11, J-30-1): whether an era's *recognition* by the realm is itself drawn.

## 1. What exists, as coded

(Execution evidence is in §12; line numbers are at the SHA above.)

**Strife (built, shipped).** A move is an Event whose kind is in `rosters.yaml: strife_kinds` `opens` or `joins` (`:3388-3393`). The world reading also opens a strand on a challenger's or outsider's `march.declared`, a `person.died` caused by `fight` or `accept`, and the second `succession.claimed` or `petition.filed` on one matter (`world_q.py:4768-4817`). Moves link by a shared referent, a one-rung step, or the same doer (`_links`, `:5068`); a linking move merges strands, oldest id kept (`_attach`, `:5094`). A strand is read at the lowest rung covering its moves (`_strand_of`, `:5120`). It is concluded while its latest move is terminal and no open referent remains: a live `detain` or `ban` on a party, `at_war` between parties' factions, a docketed referent (`open_referents`, `:5135`; `_concluded`, `:5158`). A later move reopens it. The instrument (`harness/strife.py`) grades 40 move codes by route and by observation, and reads link order against a shuffled control (`link_profile`, `:294`).

**The era (built as a scope).** `_eras` (`world_q.py:5233`) walks every strand move placed under the realm in log order; the first opens the era; a terminal move whose place is the realm rung, not the era's first, with no open referent among the era's realm-rung moves, closes it; the next move opens another. `Era` is `(id, moves, strands, concluded)` (`:4929`). Nothing in the loop reads it: `presented` (`:5267`) uses the open era to type a duchy's two slots, and that function has no loop consumer either. Between eras "nothing is of an era" (`strife-00` §4).

**The regime (built as one factor).** `commensurate(w, a, b)` returns −1, 0 or +1 from two persons' held affiliations against `data/affiliations.py::INCOMPATIBILITY`; `_credit` multiplies a told claim's confidence by `1 + regime_gain × c` at WITNESS. `incompatible_span` (`:5350`) reports whether an incompatible pair spans a strand's parties. There is no reading of *a* regime (who is in it, which institutions it holds, how large it is), so a regime cannot be seen to form, merge, split or end.

**Person side.** `flows_known` builds his strands from his ledger at kind level; `concluded_known` closes one on a `concludes` kind with no restraint he knows of; the war and docket arms are dropped person-side (`world_q.py:5403-5427`). "No era object exists in his reading" (`:5379`).

**Not built.** The unaware's field (`flow_stakes_within`, CR-100), flow salience (CR-101), office influence (CR-102, CR-104's `influence_rung`): a grep for each symbol under `engine/season/` returns no definition (§12). Natural death and the drawn year ship at their controls (`age_step=0.0`, `illness_rate=0.0`, `season_factor_draw=()`).

*(Sections 2 to 14 are appended below as the reading proceeds.)*
