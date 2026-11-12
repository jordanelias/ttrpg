# VERBS · PHYSICAL · A — custody and force: `arrest`, `capture`, `fight`, `accept`

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Parts 3–4; `U5b_VERBS_military_physical_residue.md`) — (1) **A-5, A-6, A-7, A-8** on A3's mortal-wound draw: it is drawn on the one sampler; dice come from training, so the pool is the one pool rule on the untrained default (no capability is authored for surviving a wound), and **the felled man's body band enters as levels** for or against the roll (the `wounds` source, the channel every other roll charges a wound on), with a tending ally's `healing` score as a level for; the obstacle is `mortal_wound_ob[terms]`. The text's "pool = his body band" is replaced by that; the bands, the site and the gate stand. (2) **A-16** (murder, rarely): `fight`'s contexts gain their own-motive occasion in `22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` (U5d's), whose term joins `context_terms`; the opener's edge is `U5b_PC_rulings_in_the_fight.md` §6. (3) **D-25** is closed by the ladder: an arrest needs no officer beside the prisoner; A1 is unchanged. **A-21**: a writ addressed and heard is answerable without the paper, and a challenge stays in person (`with`), both as written. **A-22, A-23**: the court must be one that may order the officer it addresses, and custody suspends a seat's acts: FA's checks, where the writ and the seat's act are formed. (4) `world_q.mustered` does not read `restrained` today (25 G-32); the conjunct is residue §4, and A2's gate needs it. (5) The mortal-wound draw is a step of the one combat calibration batch (`U5b_PC_rulings_in_the_fight.md` §5 row 5).

Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — applied `unified/U3_CONFLICT_LEDGER.md` C3-C8 and C3-R2 (`unified/work/R4_READ.md` F-R4-05): the mortal-wound draw moves **out of** `seam/wrappers/combat.py` (an adapter owns "nothing, ever", `04` §A.2; `holonic` §44.3: a wrapper that computes an outcome is a second resolver) **into** `modules/combat/`, returned on the typed outcome, its operands from `mortal_terms` (owned by `22_HAPPENINGS_A` edit 3) passed by the caller, its key `H(seed, tick, victim, "fight.mortal")` (A-30); A3 item 3's stale "pool = his body band" body rewritten to the head line (A-6, A-7, A-8); the one sampler, not "the one roller" (A-5); U1 P-13 (`mortal_wound_ob` is the obstacle member of `mortal_terms`); the payload-key roster named at the tree (`data/verbs.py:1688-1697`); the four gate files named as one test file; U3 batch split (§4.1 rows 52–54); R4 7b.0 block.
Reconciled: 2026-11-12, wave-3 mop-up (`unified/work/W3_5b_DONE.md` "For another lane", W3-1 item): A3 already reads `mortal_terms(w, pid, cause, endurance)`; the fixtures row now names the fourth cause `spell` (HAP_A's, renamed from the bout) beside the three this file draws on. The fixture's name (`mortal_wound_ob` here, `mortal_ob` in HAP_A edit 3) differs between the two files: carried to the v12 stage (U1 P-13 keeps `mortal_wound_ob`).

## Status: PROPOSED

Lands in batch: A3 (the mortal-wound draw) in B15, with the one combat calibration batch (`U5b_PC_rulings_in_the_fight.md` §5 row 5); A4 in B14 (§5 row 2, after lane A's duel chain); A0–A2 in B29, after B16 and B21 (`unified/U3_DEPENDENCY_ORDER.md` §3.1 and §4.1 rows 52–54). A3's `duel` drop lands only after A4 (the order below).
Depends on: lane A (`03_PC_duel_chain_reach.md`, B01, already built on its branch, §4.1 row 0); `22_HAPPENINGS_A_a_death_is_rare_caused_and_drawn.md` edits 3–4 (`mortal_terms(w, pid, cause, endurance)`, C3-R2); `03_PC_duel_round_and_approach_B.md` and `03_PC_exits_withdrawal_recovery.md` (B16; exits Part B points here, C3-C8); `06_FA_remit_grant_by_row.md` (B21); `U5b_VERBS_military_physical_residue.md` §4 (B22: `mustered` excludes the restrained, which A2's gate needs); `11_GO_one_draw_owner.md` (B06: the keyed draw).
Lane: PC. Tier (R4 7b.0 (1)): A3's draw and its typed outcome `opus` producer; A0–A2, A4 `sonnet`, effort `high`; one `opus` read of each gate. Test file: `engine/season/tests/test_vm_phy_a_custody.py` (four functions, one per gate of the audit's §1.7, §2.7, §3.7, §4.7; `aperture 2 s` called inside the reach readings).
Standing (R4 7b.0 (4)): the mortal pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the untrained default (A-6; no capability is authored for surviving a wound); talent as levels (A-7); the body band enters as levels through the `wounds` source (A-8). The draw takes `H(w.world_seed, w.tick, <victim id>, "fight.mortal")` (A-30). **A-81:** every band of the mortal draw writes (dies; left for dead at `max_wounds`; wounded as the scene left him), and the scene's own Event is witnessed by those present.

Folded: 2026-11-12 by `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md` (row R-4). Nothing here is deleted; one caller is named. A2 puts `capture` under a `war` or `crime` context with custody going to the authority whose act it enforces. The mass-battle lane now proposes that a beaten side's loss in flight is divided by a draw into killed and **taken** (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` §4; about half of a beaten Roman-era army's loss could be prisoners, `research/historical/mass_battle_casualties_and_results_grounding.md` A6). Named persons among the taken arrive in custody **by this proposal's custody write, under its `war` context**, with the seat that dispatched the march as the authority; the field writes no custody of its own and no second capture path. A cohort's taken share is a count on the band Event until a place for prisoners exists. Whether a person taken in a rout was captured by a draw of his own or by his unit's is that proposal's (the unit's), and the death draw of A3 item 3 is not reached by it.

Batch P-A of `audits/14_VERBS_PHYSICAL.md` §10.3. Carries that file's §1 to §4 and §0.6 (the standing
rule). Lands after lane A (`03_PC_duel_chain_reach.md`) and FA-P2 (`06_FA_remit_grant_by_row.md`).
Reference only (CLAUDE.md §0.05). Authored by Opus completing a Fable lane cut off by the usage limit
(2026-11-12).

## What it changes in `engine/season/` at runtime

1. Officers form `arrest` on persons named by warrants **addressed to them and heard of**, as well as
   warrants they hold. The licence for `arrest` and `seize` is read by one owner (A1).
2. `capture` forms only on persons, and only under a `war` or `crime` context. Its custody goes to the
   court whose warrant it enforces (A2).
3. `fight` loses its `duel` context. Its terms follow the context, and a felled party's death is a draw
   in the combat module, returned on its typed outcome (A3; C3-C8).
4. `accept` forms on challenges addressed to the person and heard of (A4).

Declared movers: every realm and spine pin in which these formations occurred (`capture`'s 26
formations, `accept`'s 37, the arrest stamp's new referents). Every season `fight` and `accept`
scene that ends in a felling under `death` terms (A3 item 3 adds draws). The corpus pins of the 13
`fight` scenes.

## The problem (evidence)

`aperture 2 0` (realm, two seasons; `scratchpad/runs/VERBS_PHYSICAL/aperture_2_0.txt`):

- `arrest` formed 1, attempted 0.
- `capture` formed 26, attempted 12, executed 0, refused 12 (`with` 7, `exists:Person` 3,
  `individual` 2).
- `fight` formed 0 (H-row at `hole_register.yaml:5321`: every `violence_context_of` reading `None` over
  three seeds).
- `accept` formed 37, refused 27 of 27 on `exists:challenge=0`.

Corpus: 13 `fight` scenes, 8 `Felled`. F-PC-04: a plain fight kills in 200 of 200.

## The resolution, decided

See the audit §1.3, §2.3, §3.3 and §4.3. Summary: one addressed-Record reader serves warrants and
challenges. `capture` gets the ruled violence decline. `fight`'s terms follow its context, and death is
drawn. The duel is `accept`'s alone.

## Exact edits, by owner

### A0 — the shared primitive (`engine/season/queries/world_q.py`)

```python
def addressed_records(w: World, p: Person, kind: str) -> tuple[str, ...]:
    """Live Records of `kind` whose addressee key (`RECORD_CONTENT["addressee"]`) is `p.id` and whose id
    `p`'s own ledger names (`person_q.ledger_names`), sorted. A Record addressed to a man who has not
    heard of it is not his business. The one owner of "addressed to him and heard of", read by the
    warrant stamp (A1) and the challenge stamp (A4). Resolver-side, read-only (`detainees_held`' shape).
    No mint, so ED-IN-0292 (1) stands."""
```

### A1 — `arrest`

| file (owner) | edit |
|---|---|
| `engine/season/queries/world_q.py` | add `warrants_for(w, actor, prisoner) -> tuple[str, ...]`: dispensations whose `terms` (via `record_sourced_operands`' `subject` key) is `prisoner` and that `actor` holds (`_held_warrants`' body, moved here from `loop/effects_information.py:948`) **or** that are in `addressed_records(w, actor_person, "dispensation")`, in tenure order then id. |
| same | add stamp term `warrants_heard(w, p)`: the persons named by `addressed_records(w, p, "dispensation")`, stamped in `_stamped` (`:3836`) under `Person`. |
| `engine/season/loop/effects_information.py` | `_eff_arrest` and `_eff_seize`: replace `_held_warrants(w, a.actor, a.verb, prisoner)` with `warrants_for(w, a.actor, prisoner)`. Delete `_held_warrants`, since nothing else calls it `[verify by grep at landing]`. Docstrings: name the addressee half and cite this file. |
| `engine/season/decision/options.py` (`:255-266`) | `warranted` is the union of today's held-claims set and the person's `warrants_heard` stamp, read off `q.referents_for("Person")` where `addressed_records` put them. Pass the stamp through the Question, not the World (AX-2). |
| `engine/season/verb_table.yaml`, row `arrest` | `requires_typed_note`: replace *"`arrest` forms only on a `subject` a HELD dispensation's `terms` names"* with *"…a dispensation he holds, or one addressed to him that he has heard of (`world_q.warrants_for`, `14_VERBS_PHYSICAL_A`), names"*. Add `payload_note`: the act's payload carries `warrant` (the Record id the effect licensed on), written by `_eff_arrest` on its Event for the reason trail. No other column changes. |

### A2 — `capture`

| file | edit |
|---|---|
| `verb_table.yaml`, row `capture` | add `referent_class: Person` and `referent_class_note: "14_VERBS_PHYSICAL_A A2: the challenge repair of 03_PC_duel_chain_reach (REM-28's precedent). Removes the exists:Person refusals. [ASSUMPTION; medium; revert: delete the column]"` |
| `rosters.yaml: violence_contexts` | add the line `capture: [war, crime]`. In the note, add: *"`capture` (14_VERBS_PHYSICAL_A): ED-IN-0337 applied to the second violent row; no `duel` (a duel is `accept`'s), no `defence` (a man defending himself does not take prisoners)."* |
| `loop/effects_combat.py::_eff_capture` (`:334`) | the `detain` object is `issuing_seat(w, rid)` of the first `rid` in `warrants_for(w, a.actor, captive)` that passes `_may_close_custody`. Otherwise it is `a.via`, as today. Docstring: "custody goes to the court whose warrant it is: `arrest`'s rule, one owner". |

### A3 — `fight` (and the scene for `capture`/`accept`)

| file | edit |
|---|---|
| `rosters.yaml: violence_contexts` | `fight: [war, crime, defence]` (drop `duel`). Note: *"`duel` dropped (14_VERBS_PHYSICAL_A A3): the challenger holds every challenge he issues, so the context licensed him to attack under lethal terms without acceptance; a duel is `accept`."* |
| `rosters.yaml` | new roster `context_terms` (`duel_terms`' shape): `war: death`, `crime: yield`, `defence: yield`. Loader: each key a `VIOLENCE_CONTEXT_READERS` name, each value a `duel_terms` value, refused at import otherwise (`data/verbs.py`, beside `WARRANT_SOURCED`'s check). |
| `decision/options.py::opening_set` | when the violence decline admits a referent, record the context name on the Candidate's payload as `context`. *(W3-4a: the roster named at the tree.)* The payload keys a formation sets are named in `data/verbs.py` beside `ORDER_ROLE_KEY`, `ORDER_RETREAT_KEY` and `MARCH_POSTURE_KEY` (`:1688-1697`), each with its closed range; `context` is declared there as `CONTEXT_KEY` with its range `tuple(VIOLENCE_CONTEXT_READERS)`. It is **not** a `choice_sourced` key (the violence decline sets it; the chooser does not choose it), so it does not enter `CHOICE_RANGES`/`CHOICE_CARRIER`. `[UNVERIFIED: whether a closed roster of payload keys exists beyond those constants; grep `payload` in `data/verbs.py` and `data/rosters.py` at landing]` |
| `seam/wrappers/combat.py::combat_input` | terms = `duel_terms[verb]` if present, else `context_terms[payload["context"]]` if present, else `death`. One path (CP-T03-09's `terms` path). The host also passes the mortal operands on the typed input: per party, `mortal_terms(w, pid, cause, endurance)` (`22_HAPPENINGS_A` edit 3; the endurance passed by the caller, C3-R2). |
| `modules/combat/` (the last step of the scene, before the typed outcome is returned) | **the mortal-wound draw** *(W3-4a, C3-C8: moved from `seam/wrappers/combat.py`; an adapter writes nothing and resolves nothing, `04` §A.2, `holonic` §44.3)*: a pure function `mortal_wound(outcome, rng, terms) -> MortalResult` (a typed record: per party `mortal: bool`, `wounds`), run for each party with `felled` true, on the one sampler (`roll_net_continuous`, A-5): pool = the one pool rule on the untrained default; the felled man's body band (`band_floors` over `Person.body_ceiling`) as levels through the `wounds` source, a co-located ally's `healing` score as a level for (A-7, A-8); obstacle = `mortal_wound_ob[terms]`, the obstacle member of `mortal_terms` (U1 P-13). Failure: `felled` stays true (dies). Partial: `felled` false, `wounds = max_wounds` (left for dead; the lasting mark follows, CP-T03-07). Success and better: `felled` false, wounds as scene. The draw is keyed `H(w.world_seed, w.tick, <victim id>, "fight.mortal")` through the one draw owner (A-30), not the private per-round stream. `seam/wrappers/combat.py` only maps `MortalResult` onto `felled`/`wounds` |
| `data/fixtures.py` | `mortal_wound_ob: {death: <swept>, yield: <swept>, blood: <swept>}` (the three causes this file's A3 draws on; `mortal_terms`' closed roster `mortal_causes` also holds `spell`, `22_HAPPENINGS_A` edit 3's illness cause, whose obstacle value is that file's, and this file's draw never passes it), swept, `H-` row for its source (U1 P-13: the fixture is this file's; `mortal_terms` reads it). The shipped values are chosen by the gate's sweep, not written here. |
| `engine/season/tests/test_cr87_violence_contexts.py` | re-point the duel positive control to `accept` (A4). Assert `fight` does **not** form for a challenger on his own challenge. |
| `verb_table.yaml`, row `fight` | `writes_source_note`: append *"the per-party `felled` is the combat module's AFTER the mortal-wound draw (14_VERBS_PHYSICAL_A A3): a felling is not a death with certainty (standing rule, 2026-11-12)."* No band, cell or kind changes. |

### A4 — `accept`

| file | edit |
|---|---|
| `queries/world_q.py` | stamp term `challenges_heard(w, p)` = `addressed_records(w, p, CHALLENGE_KIND)`, stamped under `Record` in `_stamped`. |
| `verb_table.yaml`, row `accept` | `referent_class_note`: replace the sentence beginning *"⚠ A CHALLENGE IS MINTED INTO THE CHALLENGER'S HAND"* through *"…until H-229's `give` reaches the realm."* with *"A challenge is minted into the challenger's hand. The challenged forms `accept` on it once he has heard of it (`world_q.challenges_heard`, 14_VERBS_PHYSICAL_A A4); the cell asks nothing of holding."* |

### Order of landing

A0, then A1 (one commit: the reader, the stamp, both effects, the formation). Then A2. Then A4, then
A3 (the `duel` drop must not land before A4, or no route to a duel exists in between). The mortal draw
in A3 may land alone, first, since it is independent of reach.

## Gate (execution artifacts)

The audit's §1.7, §2.7, §3.7 (including the standing-rule gate) and §4.7, as four functions of one test
file, `engine/season/tests/test_vm_phy_a_custody.py` (R4 7b.0 (3)). A3's function also asserts the
draw's site: a planted wrapper-side draw (`seam/wrappers/combat.py` computing `felled`) is absent, and
the module's `MortalResult` is what the wrapper maps. Plus `aperture 2 0` and `aperture 2 1` before and after, quoted in the commit:
`capture` refusals on `exists:Person` equal 0, `accept` refusals on `exists:challenge` equal 0, and
`arrest` and `capture` formed and attempted as measured.

## Falsifier

The planted failures named in each gate: revert to `_held_warrants`, delete the `capture` roster line,
restore `duel`, bypass the mortal roll, and return `()` from `challenges_heard`. Each must turn its test
red. The control `mortal_wound_ob` at an unreachable value must reproduce 200 of 200 deaths in the
F-PC-04 probe.

## NERS reading

- **N.** It turns custody, hostages, duels and survivable violence from built-but-unreached into play.
  Cut test per verb: audit §1.9 to §4.9.
- **R.** Beaten survivors exist (resentment, ransom, pardon, return). Courts hold people. The no-player
  half produces crimes, arrests and feuds.
- **S.** One addressed-Record reader. One licence owner for `arrest`, `seize` and `capture`'s custody.
  One terms path. One sampler for the mortal draw, in the module that owns the scene.
- **E (last).** Two readers, two stamps, two roster lines, one roster, one draw, against four verbs
  brought into play. High.

## Cost class

Build: two `world_q` readers and two stamps, an effect edit in two modules, one module-side draw with
its typed outcome, one fixture, roster lines. Declared re-records of the season pins named above.
