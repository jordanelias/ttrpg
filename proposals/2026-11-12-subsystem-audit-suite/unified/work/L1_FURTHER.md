# L1_FURTHER — Layer 1 sentences checked against A-100, A-101, A-105, A-107, A-108, A-112

## Status: WORK RECORD (the A-104/A-97 follow-up lane, 2026-11-12; reference, resolves nothing at runtime, CLAUDE.md §0.05; deleted with `unified/work/` when v12 is adopted)

Reconciled: 2026-11-12, A-104/A-97 follow-up.

**Method.** `grep -rn` (and `grep -rnw` for short words) over `architecture/` (every `.md`: `meta/00`–`10`, `04`,
`holonic_ARCHITECTURE.md` (`hol`), `ARCHITECTURE_V2.md`, `PLAN.md`, `VOCABULARY.md`, `00_ADOPTION_README.md`,
`01_NPC_VS_ARC.md`) for each ruling's words: A-100 `mass battle|field provider|lanchester|pool|obstacle|Ob`;
A-101 `round|rounds|exchange|duel|bout|engagement`, `per round|next round|this round`; A-105
`reduc|re-grant|re-stamp|granted_acts|revocation|revoke`; A-107 `trait|moved_by|resonant_style`; A-108
`manner|rigid|grandiose|deontolog|identically|pursuit … project`; A-112 `facult|attribute|skill`. Each hit was read
in context. Line numbers are after this lane's edits (no line was added to any `architecture/` file; `wc -l`: `04`
1658, `hol` 2077, `PLAN.md` 2097, all unchanged).

## Applied (the ruling plainly requires it; both halves; convention of `L1_APPLIED.md`; ledger `ED-IN-0360`)

| node | ruling | the sentence, as it read | why it contradicted | applied |
|---|---|---|---|---|
| `L1-A105` | A-105 (a grant reduction is judged as a revocation) | `04:604-605` §C.2: "via is a Seat whose `conferral` basis reaches it, opening or re-granting a `hold` ON that seat -- conferral (`ED-IN-0277`)"; twin row 10a `04:1036` (§C.2 "is the current, complete enumeration") | §C.2 admits ANY re-grant on the conferral basis, so a re-grant that narrows a sitting holder's grant passes as a conferral; A-105 rules it a revocation, and `IS-B3-FA-07` step (1) makes the gate return `T_O` there, which §C.2 as written would forbid (the code would refuse a write the "complete" enumeration admits) | `04:605` gains: a re-grant to the sitting holder that drops an act his grant carried is a REDUCTION, judged as a revocation (T-o, `via` present), never admitted as a conferral; row 10a gains the same clause. The power-relation odds are the verb's draw (`revoke`'s contested row, `IS-B3-FA-07` step 2), not the gate's, so nothing about them enters Layer 1. Residual: `04:576`, a historical comment ("`conferral` … a seat-authorized OPENING or re-grant of a `hold` on that seat"), sits in the same pseudocode block as the amended `:605` and is left as the record of what the basis was built as |
| `L1-A107` | A-107 (traits are a separate roster, held on a new `Person.traits`) | `04:234-236` §B.2: `Person := ( id, weight, capability, body, exists, travel_leg , stance[], pursuits, scar[axis], axis_count[axis], coherence?, heritage? , ledger )` | the ruling names a new carrier field that the Layer 1 type does not declare; the tree's precedent for a new field is that the tuple gains it (`heritage?`, CR-30, `04:239`) | `:235` gains `traits`; `:241` carries the mark: the `moved_by_*` dispositions, a closed roster apart from the skills in `capability`, own loader, gives no dice. **No PART D twin**: no PART D row lists Person's fields (rows 1–53 read); `hol` §9 (`hol:324`) is the older tuple (`marks[]`, `convictions`, `beliefs[]`, `ties_index`), already superseded by `04` §B.2 and not amended for `heritage?` either; left as it stands |
| `L1-A108` | A-108 (a stored offset per manner axis) | the same tuple | as A-107: a stored per-person value with no declared field | `:235` gains `manner_offset?` (optional: absent = what `pursuits` project, as before); `:241` carries the mark. The field name is `IS-B2-CHAR-07`'s (`state/carriers.py::Person.manner_offset`), not Jordan's; `[ASSUMPTION: the name follows the instruction item; reversible by renaming in both places]` |

## Checked, not contradicted

| ruling | sentence | why it holds |
|---|---|---|
| A-100 | `hol:1406-1407` §39.4 and `03_VERBS_AND_LOOPS.md:274` §E.3 ("One degree ladder for every scale … A duel, a debate, a siege and an examination all use it"); `PLAN.md:377` (H-31, quoting the same) | the ladder grades the margin or (A-3, `L1-A3`) the field's end state; A-100 changes how a field exchange is drawn (a damage distribution), not how its outcome is graded. Nothing in Layer 1 says a field exchange is a pool thrown at an obstacle |
| A-100 | `01_AXIOMS.md:448` (*obstacle*: "the `Ob` a pool is thrown at") | a definition of the word, not a claim that the field uses one |
| A-112 | no hit for `facult` in `architecture/`; `hol:347` §9.2 ("`rank` contributes to a pool") | Layer 1 names no `faculty`; the skill rank supplies dice, as A-112 has a combatant's skill scores read through the skill table |
| A-108 | `04:1167` F.8 ("two venues with identical seats must decide identically"); `01_AXIOMS.md` "identically" hits | about venues and witnessing, not about persons' manner |
| A-105 | `04:337-338`, `:369-370`, `:407-412`, `:603` (`Seat.revocation`, T-o) | the revocation basis is unchanged; A-105 routes a reduction INTO it |

## For Jordan (a word, not a rule; not applied)

| ruling | sentence | the conflict | why not applied |
|---|---|---|---|
| A-101 | `04:1065` row 36 ("Where several scenes claim one person's **round**, office rank is a declared weight …", text added by `L1-A64`) and `hol:1166` §33 (the same clause) | "round" here is the season's within-season pass, which the glossary now calls a **lap** (`unified/U1_GLOSSARY.md:140`, `:404`); A-101 takes "round" for one engagement of a fight. The rule is not contradicted (row 36 is about scene precedence, not fights); the word fails the glossary's word test where both senses meet | A-101 rules the fight, not the season's vocabulary; the identifiers' rename is the candidate PCR-4 (`master/pc_round/PC_ROUND_SPEC_part2.md` §6, unscheduled, "the rest change at their next edit"). Changing Layer 1's word is a vocabulary amendment no ruling orders; listed for Jordan or v12's rename batch |
| A-101 | `03_VERBS_AND_LOOPS.md:126` ("**interaction** \| one exchange resolving \| the verb") | "exchange" is A-101's word for one attack and its defence in a fight; here it is the generic sense (one interaction resolving) | the same: a word overlap at season scale, no rule contradicted |
