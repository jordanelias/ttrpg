# CANDIDATE — pursuit/axis cells and character migration (draft, 2026-09-27). RATIFIES NOTHING. Every cell either cites its source or is marked null with a stated reason. Pending Jordan's approve/vet.

## Status: **FOLDED INTO THE BUILD (v9; Jordan 2026-10-06, RS-1; ED-IN-0291) — the source of IN-08's cells (B-G); the authoring surface until that commit lands, then retired with `proposals/2026-09-18-character-decision-layer/PROPOSAL.md` by its `FORK:` rows. The pursuit `faith` is `doctrine` (its row PROVISIONAL, RS-3) and `warden` is `stewardship` (RS-4). Not wired to anything until IN-08 lands; reference under `CLAUDE.md` §0.05.**
## Revision 5 (2026-09-27): **the `faith` row is ENACTED on Jordan's own formulation**, verbatim: *"faith would just be someone's orientation towards pursuing actions/decisions that concern faith, be it agnostic pursuit of Truth, a Solmund zealot doing things that respect the religious tenets, an atheist trying to shut down or discredit religions, or an Einhir revivalist pursuing its revival."* `faith` is the MAGNITUDE of orientation toward religious matters, not the DIRECTION (which is `Person.conviction`) and not the DISPOSITION (which the person's OTHER pursuits carry). §2.11: R/F and G/Hu → 0 as instructed; P/S and Se/Sl → 0 on the same logic (§2.11 says why); Pa/Eq +0.2 and D/I −0.3 stand, outside the instruction, with the consequence flagged. §5.2 re-run: **arm A now SEPARATES (+0.229)**; B and C fail by a hair (+0.524, +0.527) for a reason the row cannot fix. §5.3 re-run. This closes the "recommended, not enacted" thread of revs. 2–4.
## Revision 4 (2026-09-27): **the grading method is escalated, on Jordan's instruction, and supersedes rev. 3's row-by-row re-check.** Three phases in order: **§1a PHASE 1** defines all 29 terms (15 pursuits, 14 poles) by etymology and by their standing in political theory and sociology, naming the tradition where one exists; **§1b PHASE 2** compares them for genuine independence — axis vs axis (where the +0.776 and +0.755 correlations are resolved BY DEFINITION), pursuit vs pursuit, and pursuit vs axis-name (where the justice/equitable identity ban is grounded); **§2 PHASE 3** then re-grades every cell against that grounding — each cell says CONFIRMED or CHANGED, and every `reasoned` cell now points to the Phase 1/2 entry it rests on beneath any corpus citation. Ten values changed in Phase 3 (listed at §2.16; the tenth, warden H/E, follows Jordan's same-day ruling that `warden` refers specifically to the Southernmost, recorded at §1a); rev. 3's three R/F moves are re-derived there rather than assumed. §5.2/§5.3 re-run on the Phase 3 grid, with one paragraph (§5.3) on whether the grounding reduced the correlation defects or explains why they stand. Jordan's narrower correction on how the equity rule is STATED (the ban is on treating the pursuit as IDENTICAL to the axis, not on the vocabulary or on S3's numbers as corroboration) is applied at §0.4 and §7.3 and grounded at §1b(c).
## Revision 3 (2026-09-27): Jordan supplied his own definitions of `precedent/substantive` and `rigid/flexible` (recorded verbatim at §0.5) as the disambiguating test for rev. 2's +0.776 correlation. The 11 same-sign rows were re-examined one by one against that test with registry evidence: **three moved** (liberty, individuality, love: R/F → rigid; P/S unchanged), **seven re-examined and kept** (honour, stability, family, warden, community, happiness, wealth — each row's R/F cell now says so), **one left for the H7 pass** (faith). §5.2/§5.3 re-run; the correlation fell +0.776 → +0.284 and both of Jordan's missing corners are now populated (§5.3).
## Revision 2 (2026-09-27, on Jordan's instruction via the coordinator): **the 15×7 grid now has ZERO nulls.** The 47 nulls and 4 two-way CONFLICT cells of revision 1 each carry ONE value under a fourth grade, **REASONED** (§0.2) — no corpus citation, placed by stated definitional/analogical reasoning, never silently. Every `partisan↔equitable` cell was re-grounded in **social justice as a substantive concept** (distributive fairness · treatment under law · structural equity in outcomes) rather than the axis's own label; the cells whose VALUE changed for that reason are listed in §7.3. §5's self-check was re-run on the completed grid and **the pair now fails at every arm** — reported, with the cause, not tuned away. The alignment table (§3) is out of this revision's scope and stands as revision 1 left it.
## Authority: **none.** Nothing here lands until Jordan approves it; the owners it would land at (`engine/season/rosters.yaml` `tables.pursuit_projection` / `tables.alignment` / `tables.role_template_pursuits`, `references/descriptor_registry.yaml`, `references/npc_registry.yaml`, `proposals/2026-09-20-pursuit-basis-worksheet.yaml`) are **untouched** by this file.
## Scope: C1 (105 projection cells + 42×7 alignment), C2 (npc_registry + role-template migration, and the H7 pair), and a recommendation on G-Q5 — per `PROPOSAL.md` §3.3 and §5.
## Method: **corpus-mined, not invented**, in the discipline `rosters.yaml:1367` sets for `role_template_pursuits` ("TRANSCRIBED, NOT INVENTED"). Where a magnitude is mine it says so. Where nothing in the tree speaks, the cell is `null`.
## Grade under `CLAUDE.md` §0.2: `paper` for every cell; `measured` for §5's self-check and the harness readout, which name the command.

---

## §0 · How to read this file

### 0.1 Sign convention (an ASSUMPTION this file makes and Jordan should confirm)

`pursuit_axes` are bipolar with the negative pole named first (worksheet `:76-83`). This file writes a
cell as one number in `[-1, +1]`: **negative = engages the first-named (neg) pole, positive = the
second-named (pos) pole.** So `hierarchical -0.9` on the old table becomes `-0.9` on
`hierarchical↔equal` (unchanged), and old `traditional +0.8` becomes `-0.8` on `precedent↔substantive`.
`PROPOSAL.md:429` already reads `deontological` as the NEG pole for H2, which this matches.
`score = Σ axis_w · align` (`choose.py:365-368`) then rewards a hierarchical person (axis_w < 0) for a
hierarchical act (align < 0). ⚠ If Jordan prefers positive = first-named, every number in §2 and §3
flips sign uniformly; nothing else changes.

### 0.2 Grades

| grade | means |
|---|---|
| **cited** | the number is transcribed from a source that already holds it (PP-687's matrix via `rosters.yaml:1449-1513`; `candidate_basis_v1.json`; a ruling text that fixes the value), with at most a sign flip per §0.1 |
| **derived** | the DIRECTION is read off a cited source's prose; the MAGNITUDE is mine and is flagged |
| **analogy** | as *derived*, but the source is a nearest OLD row that is NOT this pursuit's lineage (`was: null` in the worksheet) — e.g. `Equity` for `justice` |
| **reasoned** | **no corpus citation.** Placed by explicit definitional or analogical reasoning, stated in the cell: *"[pursuit]'s definition implies [pole] because …"*. Jordan's instruction (rev. 2): a placement with stated reasoning is acceptable; a silent guess is not. Every rev. 1 null in §2 is now this grade |
| **null** | no citable basis found. **Zero remain in §2**; the grade survives only in §3 (alignment, out of rev. 2's scope) |
| **CONFLICT → resolved** | two sources disagreed on sign in rev. 1; §2 now shows ONE value with the resolution reasoned in the cell, and §7.2 records what each source said |

### 0.3 Sources (S-numbers used throughout)

| id | source | status |
|---|---|---|
| S1 | `engine/season/rosters.yaml:1449-1513` `pursuit_projection` — the 13×4 PP-687 matrix, byte-identical to `.designs/systems/characters/reference/conviction_axis_matrix_v30.md` §2, whose §3 carries the per-cell rationale | live table (old basis); the rationale doc is **quarantined `.designs/`**, read as a source for this draft only |
| S2 | `engine/season/rosters.yaml:1515-1662` `alignment` — the old 52 verb×axis cells, each with a one-line reason (`H-66`: "a reason is not a citation") | live table (old basis) |
| S3 | `proposals/2026-09-16-conviction-decision-layer/candidate_basis_v1.json` — a 13×4 placement over `memory / substantive / equity / selfish`, placed 2026-09-16 by an agent given only the taxonomy; `RULINGS.yaml:1093-1097` records Jordan ruling those four as "THE AXES" on 09-17, superseded by the seven on 09-20. Its own `_null_finding` says `selfish` is near-inert on the old roster by design | one model's placement, not canon; carries the only existing numbers on three of the new axes |
| S4 | `registers/editorial_ledger_in_archive.jsonl:177` (ED-IN-0261) — the ruling text: the fifteen, the seven, `stability` orthogonal to hierarchical/equal, self/other "lives in the pursuit space (wealth, reputation, individuality against community, family, love)", the `faith` pair | ruled |
| S5 | `proposals/2026-09-20-pursuit-basis-worksheet.yaml` — `was:` rows (`:107-121`), Jordan's verbatim axis definitions (`:62-68`), the pair (`:123-137`) | authoring surface |
| S6 | `references/descriptor_registry.yaml:279-287` `axis_roster` — old `instrumental` glossed "+ end-justifies-means, calculative · − principled, **deontological**" | live registry |
| S7 | `references/npc_registry.yaml` `convictions:` blocks (lines cited per character) | live registry |
| S8 | `.designs/systems/characters/reference/conviction_taxonomy_v30.md` §2, §2.1, §2.3, §6 — definitions of the thirteen; "Greed and ambition are not Convictions" | **quarantined** |
| S9 | `.designs/systems/npcs/reference/npc_behavior_v30.md` §2 — per-NPC Ethical Framework rows and conviction glosses (Ehrenwall `:58`, Baralta `:99-101`, Vaynard `:119-121`, Vossen `:161-163`, Guilds `:261-263`, Haelgrund `:311-313`) | **quarantined** |
| S10 | `.designs/systems/factions/reference/faction_canon_v30.md` §4 (`:184-199`) — the six role templates (PP-686 §3.3.1) | **quarantined**; already transcribed live at `rosters.yaml:1381-1417` |
| S11 | `proposals/2026-09-18-character-decision-layer/PROPOSAL.md` §2.2 (`bend_price` collapse), §2.4, §3-§4, §6, §8, §9; `proposals/2026-09-16-conviction-decision-layer/synthesis.md` §1.3, §2; `adjudication_register.yaml:189-265, 544-593`; `proposals/2026-09-18-the-gather/03_DECISIONS.md` §2, §4 | proposals (reference) |
| S12 | `canon/philosophy/` — grep for the fifteen names: hits are about drift propagating to kin/community (`07_drift.md:290-308`, `04_being_persistence.md:137`, `RULINGS.md:377-378`) and "Not virtue. Standing." (`07_drift.md:207`). **Nothing there constrains an axis placement**; recorded so the search is not re-run | canon; no cell rests on it |
| S13 | `engine/season/verb_table.yaml:100-836` — the 38 verb rows (stratum, eligibility, beneficiary, requires, the reasons in their notes) | live table |

### 0.4 What the old axes become (the lineage rule, applied throughout §2)

| old axis (S1/S2) | new axis | how carried | why |
|---|---|---|---|
| `hierarchical` | `hierarchical↔equal` | value unchanged in sign (old `+` = rank = neg pole, which is `−` here per §0.1: **so old `+0.4` → `−0.4`**) | STR-2 measured "Equality = hierarchical flipped at r = −0.971" on an independent placement (`adjudication_register.yaml:630-633`) |
| `traditional` | `precedent↔substantive` | old `+t` → `−t` | S3's `memory` column correlated r = +0.85 with old `traditional` (`candidate_basis_v1.json:4`); Jordan's `precedent` definition is *"what actions have been performed in similar situations prior"* (S5 `:65-66`). ⚠ **Not identical**: traditional = ancestral vs reformist; precedent = where you look for the answer. Worksheet `:94-96` says `was:` "is NOT a migration". Cells carried this way are graded **cited** with this caveat attached once here rather than 15 times |
| `instrumental` | `deontological↔instrumental` | value unchanged | S6 glosses the old axis's negative pole as "principled, **deontological**" — this is the one axis with a literal lineage |
| `sacred` | — | **dropped**; moves to `Person.conviction` (S4, S5 `:85-89`) | not carried into any pursuit row. Where an S2 verb cell's REASON was really about binding/vow rather than the numinous, it is re-homed to `deontological↔instrumental` and says so |
| — | `partisan↔equitable` | S3's `equity` column is legitimate NUMERIC corroboration, and equity vocabulary is the right vocabulary for describing what a pole literally named `equitable` measures. **The rule (Jordan, restated rev. 4) is narrower than "avoid the word": a pursuit's substantive content must not be treated as IDENTICAL to the axis's name.** "Justice pursues equity; equity is the equitable pole; therefore high" is banned because it is circular — it restates the axis under the pursuit's label and gives the pursuit no independent content. What a Pa/Eq cell needs is the pursuit's OWN content (for `justice`, the three social-justice strands: distributive fairness · treatment under law · structural equity in outcomes) and then an argument for how that content bears on a disposition of TREATMENT (impartial vs for-one's-own). §1b(c) grounds the distinction; §7.3 lists the cells rev. 2 changed under it | S3 kept as corroboration wherever the independent reasoning agrees; moved where it does not |
| — | `selfish↔selfless` | S4's ruling (six pursuits named) + S3's `selfish` column | S3's own null finding: near-inert on the OLD roster *by design* (S8 §2.3 factored self/other out) — so S3's near-zeros are a cited "no lean" for lineage rows, and the six NEW placements come from S4 |
| — | `rigid↔flexible` | no numeric source anywhere | S11 §2.2 collapsed rigidity/flexibility/pragmatism into ONE field `bend_price` on 09-18, and ED-IN-0261 then made it an axis on 09-20 with no cells. Mostly null |
| — | `grandiose↔humble` | no numeric source anywhere | `synthesis.md` §2 / CAT-9: humble↔vain is *regard inverted* — "acts that put him in front of witnesses". Mostly null |

### 0.5 Jordan's definitions of `precedent/substantive` and `rigid/flexible` (verbatim, 2026-09-27, via the coordinator)

Recorded beside the two he gave on 2026-09-20 (S5 `:62-68`), and binding on every P/S and R/F
cell in §2 from rev. 3 on:

> "precedent means you return to previous ideas/actions for resolution while substantive means you
> forge unprecedented new ones. rigid means that you are unwilling to deviate from your course of
> action in the face of difficulties while flexible means that you will. there is overlap but a
> flexible person who relies on precedent will try to find other historical approaches to do
> something and a rigid substantive person will refuse to deviate from their new idea."

**The test this gives.** P/S is WHERE the answer comes from (the past vs a new idea); R/F is
whether the chosen course is HELD when it gets hard. Two corners must be populated for the axes to
be two: **flexible + precedent** — one historical approach fails, go find a different one — and
**rigid + substantive** — invented your own answer, now won't budge from it. Rev. 2 had placed 11
of 15 rows with P/S and R/F the same sign (r = +0.776), i.e. it had read "looks to the past" as
"holds its course" — one disposition under two names. §2's R/F cells were re-examined row by row
against this test (each says whether it MOVED or was KEPT, and on what evidence); §5.3 reports the
result.

---

## §1 · The verb set this file cells (42)

`verb_table.yaml:100-836` holds 38 rows: carry · commit · comply · confer · convene · create_record ·
destroy_record · determine · dispatch · establish · evade / defy · exchange · forge · issue ·
**kill / wound** · levy · move · oblige · open_case · petition · construe · release · repudiate · restore ·
revoke · speak · succeed · tell · examine · interview · research · surveil · thread_read · reconstruct ·
tie / knot · transfer · utter · work. Minus `kill / wound`, plus `kill`, `wound`, `fight`, `challenge`,
`accept` (ED-IN-0261; `PROPOSAL.md:659`) = **42**. 42 × 7 = **294** alignment positions.

---

## §1a · PHASE 1 — Definition and etymology, once per term (29 terms)

Written before any grade was touched (rev. 4). For each term: **(a)** etymology — root, original
sense, drift; **(b)** how contemporary political theory and sociology define it, naming the tradition
or thinker where one exists, and saying so where the word is ordinary-language rather than technical;
**(c)** where Valoria's stated definition (S5 `:62-68`, §0.5, S8 §2) departs from or narrows the
standard sense — the departure matters for Phase 2. Nothing here is a Valoria citation; it is the
outside literature the grid is checked against.

### 1a.1 The fifteen pursuits

**virtue.** (a) L. *virtus*, from *vir* "man": manliness, valour; by Cicero "moral excellence", the
Latin rendering of Gk *aretē* (excellence of any kind, then of character). Christian usage added the
theological virtues; Machiavelli's *virtù* (efficacy, boldness) split off a non-moral sense. (b) The
Aristotelian tradition: a virtue is a stable excellence of character, a disposition to feel and act at
the mean, chosen by practical wisdom (*phronesis*) in the particular case (*NE* II–VI). Revived by
Anscombe ("Modern Moral Philosophy", 1958), MacIntyre (*After Virtue*, 1981: virtues sustained by
practices, a narrative life, and a tradition), Foot, Hursthouse. Two features matter here: virtue
ethics is explicitly a THIRD way beside deontology and consequentialism (Anscombe's point), and
Aristotle's list includes *megalopsychia* — greatness of soul, a proper pride — where the Christian
list includes humility. (c) Valoria fixes the Aristotelian sense (S8 §2.1: "*virtù* in the
Aristotelian sense, distinct from Machiavellian"), so the Machiavellian sense is out.

**honour.** (a) L. *honos/honor*: esteem, and the public office that expresses it (*cursus
honorum*); OF *honor*; "honour" as a pledged code is medieval-chivalric. (b) Anthropology of the
Mediterranean: Pitt-Rivers ("Honour and Social Status", 1965) — honour is "the value of a person in
his own eyes, but also in the eyes of his society", a CLAIM to worth plus its ACKNOWLEDGEMENT;
Bourdieu (*Outline of a Theory of Practice*, the Kabyle "sense of honour") — a habitus of challenge
and riposte, obligations of generosity, honour as symbolic capital; Stewart (*Honor*, 1994) — a
right to respect; Appiah (*The Honor Code*, 2010) — honour codes change by "moral revolutions" but
bind their holders absolutely while in force; Nisbett & Cohen on cultures of honour. Honour is
stratified (a knight's, a merchant's) and public. (c) Valoria keeps the code/oath half and splits the
acknowledgement half off as `reputation` (S4), so honour here is Pitt-Rivers's CLAIM side.

**liberty.** (a) L. *libertas*: the legal status of the free man as against the slave — freedom as
NON-SUBJECTION, before it meant non-interference. (b) Berlin ("Two Concepts of Liberty", 1958):
negative liberty (absence of interference) vs positive (self-mastery); Constant (1819): liberty of the
ancients (participation) vs the moderns (private independence); the republican revival — Skinner,
Pettit (*Republicanism*, 1997): liberty as NON-DOMINATION, the absence of arbitrary power over one,
which is the original *libertas*; Mill (*On Liberty*, ch. 1) the harm principle. (c) Valoria's
"self-determination, freedom from imposed authority" (S8 §2; S1 §3.7 "*libertas*") is Pettit's
non-domination plus Berlin's negative liberty — a CONDITION one is in, not a use one makes of it
(that use is `individuality`, below).

**justice.** (a) L. *iustitia*, from *ius* "right, law"; Ulpian's *suum cuique tribuere* (render
each his due), carried by Aquinas as the cardinal virtue "a constant and perpetual will to render each
his due". "Social justice" is 19th-c. (Taparelli, 1840s), naturalised by Rawls. (b) The central
contested concept of political theory: Rawls (*A Theory of Justice*, 1971 — justice as FAIRNESS,
chosen behind a veil of ignorance, so impartial by construction; the difference principle is
distributive); Nozick (entitlement, historical not patterned); Sen (*The Idea of Justice*, 2009 —
comparative, remove manifest injustice); Walzer (*Spheres of Justice* — distributive criteria differ
by sphere and by COMMUNITY); Young (*Justice and the Politics of Difference* — STRUCTURAL injustice,
claimed by groups); Fraser (redistribution vs recognition); Tyler on PROCEDURAL justice (people accept
outcomes from fair procedures). Three strands used in this file: distributive fairness, treatment
under law, structural equity in outcomes. Retributive justice is a fourth and is the one most easily
carried partially ("justice for my people"). (c) Valoria gives no definition; §2.4 uses the three
strands. Note that justice is an END-STATE of institutions (Rawls's "basic structure"), which is why
§1b(c) can separate it from a disposition of treatment.

**wealth.** (a) OE *wela* "well-being, prosperity" (cognate with *weal*, and with "well"); "wealth"
= welfare until the 14th c., then material riches. The word and `happiness` share a root sense of
faring well. (b) Largely ordinary-language; the theoretical literature is on its PURSUIT: Aristotle
(*Politics* I) *chrematistics* (acquisition for its own sake, unlimited) vs *oikonomia* (household
provision, bounded); Weber (*The Protestant Ethic*) — ascetic accumulation WITHOUT enjoyment or
display; Veblen (*Theory of the Leisure Class*) — conspicuous consumption, wealth AS display; Marx on
accumulation; Bourdieu — economic capital convertible into social and symbolic capital. (c) S8 §2.3
had ruled greed not a conviction; S4 reverses this by making `wealth` a pursuit.

**reputation.** (a) L. *reputatio* "a reckoning, consideration" (*re-* + *putare* "to reckon");
"the estimation in which a person is held" from the 16th c. (b) Goffman (*The Presentation of Self*)
— impression management; Bourdieu — symbolic capital, "distinction"; Origgi (*Reputation*, 2018) —
reputation as a social information good, the second self that lives in others' minds; Ridgeway —
status characteristics; signalling economics. Distinct from honour (Pitt-Rivers): reputation is the
ACKNOWLEDGEMENT half alone, and can be managed strategically. (c) Valoria renamed `status` to
`reputation` (S4) precisely as the concept contrasting with `standing_of`'s computed gap.

**scholastics.** (a) L. *scholasticus* "of the school", Gk *scholē* "leisure → lecture-place";
"scholasticism" names the medieval school method — *lectio*, *quaestio*, *disputatio* — reasoning
FROM AUTHORITIES (Aristotle, the Fathers) toward new conclusions. (b) Weber ("Science as a Vocation")
— the ethos of inquiry as its own calling; Merton (1942) — the four norms of science: universalism,
communism (shared findings), disinterestedness, organised scepticism; Kuhn on paradigms (normal
science works inside an inherited framework); Bourdieu (*Homo Academicus*, the "scholastic point of
view"). (c) Valoria's "reasoned inquiry, learning, scholarly method" (S8 §2) is Merton's ethos more
than the medieval method — but the WORD carries the medieval method's authority-boundness, which is
why P/S is a genuine question for it.

**stability.** (a) L. *stabilis*, from *stare* "to stand": that which stands firm. (b) Political
science: Huntington (*Political Order in Changing Societies*, 1968) — order as institutionalisation,
prior to the form of the order; Lipset on legitimacy and stability; Weber's "legitimate order" as
what is stably obeyed. The DISPOSITION toward it is conservatism: Burke (prescription; and "a state
without the means of some change is without the means of its conservation"), Oakeshott ("On Being
Conservative": a disposition to prefer the familiar, the tried, the actual). (c) Valoria's `stability`
(S4/S5 `:47`) is the pursuit of an order that persists — of ANY shape (ruled orthogonal to
hierarchy), which matches Huntington's separation of order from its form.

**individuality.** (a) L. *individuus* "indivisible" (calque of Gk *atomon*); "individual" as a
single person from the 17th c.; *individualisme* coined pejoratively by French counter-revolutionaries
and used by Tocqueville (1840) for the WITHDRAWAL of citizens into private circles. (b) Mill (*On
Liberty*, ch. 3, "Of Individuality") — self-development, "a person whose desires and impulses are his
own", against the tyranny of custom; Emerson's self-reliance; Simmel (individuality against the
metropolis); Durkheim's "cult of the individual"; Tönnies *Gesellschaft*; Lukes (*Individualism*,
1973) separates the strands. In Schwartz's value circumplex "self-direction" (independence of thought
and action) sits in OPENNESS TO CHANGE, not in SELF-ENHANCEMENT (power, achievement) — being one's own
person is theoretically distinct from serving oneself. (c) Valoria gives no definition beyond the
name; §2.9's working definition (a distinct self, not defined by station, side, kin or precedent) is
Mill's.

**community.** (a) L. *communitas*, from *communis* "shared, common" (*com-* + *munus* "duty, gift").
(b) Tönnies (*Gemeinschaft und Gesellschaft*, 1887) — community of blood, of place, of mind, bound by
natural will, against society bound by contract; Durkheim — mechanical solidarity (likeness) vs
organic (interdependence); Turner — *communitas* as the levelling bond of liminality;
communitarianism (Sandel, Taylor, Walzer, Etzioni) against liberal impartialism; Putnam — social
capital, and the distinction between BONDING (in-group, can be exclusionary) and BRIDGING capital;
Brewer — in-group love is not out-group hate and not altruism; Anderson's imagined communities. (c)
Valoria's "belonging to the immediate community; common life" (S8 §2) is Tönnies's community of place.

**faith.** (a) L. *fides* "trust, loyalty, good faith" (as in *bona fides*, fidelity); the religious
sense (belief in God) is the 14th-c. narrowing. (b) Tillich (*Dynamics of Faith*, 1957) — faith as
"the state of being ultimately concerned", which any object can occupy; James ("The Will to
Believe"); Kierkegaard's leap; Weber — the religious "ethic of conviction" (below, under
*deontological*); Durkheim — religion as the collective's self-worship; sociology of religion
separates believing, belonging and behaving (Davie, "believing without belonging"). (c) Valoria's
`faith` pursuit is exactly Tillich's INVOLVEMENT — "how much of yourself goes into religious matters
at all" (S5 `:124`) — with belonging moved to `Person.conviction` (S4). That is a real departure from
the ordinary sense, in which "faith" names a belief-content.

**happiness.** (a) ME *hap* "chance, luck" (ON *happ*) + *-ness*: good fortune, then contentment;
Gk *eudaimonia* (flourishing, a life going well) is the philosophical ancestor and does NOT mean a
feeling. (b) Two readings that the literature keeps apart: HEDONIC — pleasure/contentment, Bentham's
utility, contemporary subjective well-being (Diener, Layard); EUDAIMONIC — Aristotle, Sen/Nussbaum's
capabilities, Haybron. Schwartz's "hedonism" value sits between self-enhancement and openness. (c)
Valoria gives no definition; §2.12's working definition takes the HEDONIC reading (one's own
contentment), because the eudaimonic reading collapses into `virtue` (§1b(b)).

**family.** (a) L. *familia*: the HOUSEHOLD, including servants (*famulus* "servant"), under a
*paterfamilias* — a unit of domination before it was a unit of kinship. (b) Weber — the patrimonial
household as the root form of traditional domination; Parsons — the nuclear family's functions;
Bourdieu ("On the Family as a Realized Category"; strategies of reproduction — the family reproduces
its position across generations); Lévi-Strauss on kinship as alliance; Okin's feminist critique of
the family as a site of injustice; Williams's "one thought too many" and Nagel's *Equality and
Partiality* — the family is the canonical case FOR partiality against impartialist ethics. (c)
Valoria gives no definition; the hearth-with-a-head (§2.13) is the *familia* sense.

**love.** (a) OE *lufu*, PIE *\*leubh-* "to care, desire" (cognate with "believe", "leave" as
permission). Gk distinguishes *erōs*, *philia*, *agapē*; the English word covers all three. (b)
Frankfurt (*The Reasons of Love*, 2004) — love is disinterested concern for the beloved's good, a
"volitional necessity": the lover CANNOT will otherwise, which is a constraint on the will, not a
choice among options; care ethics (Gilligan, Noddings) — caring-for a particular other, explicitly
PARTIAL; Giddens (the "pure relationship", confluent love — contingent, revisable); Luhmann (*Love as
Passion*, a communication code); Nussbaum; Aristotle's *philia* as wishing the friend's good for the
friend's sake. (c) Valoria gives no definition; §2.14 uses Frankfurt's and care ethics'.

**warden.** ⚠ **RULED (Jordan, 2026-09-27, via the coordinator): `warden` refers specifically to
the Southernmost.** It is not the generic English word (prison warden, church warden, game warden,
feudal steward), and this entry is rooted in Valoria's own institution FIRST, with the general word
and the real-world theory as secondary framing to be CHECKED against it, never substituted for it.
(a′) **The primary referent — what the corpus establishes the Southernmost Wardens to be.** An
independent order (`faction: Independent (Southernmost Wardens)`, S7 `:798`) of thread-sensitive
practitioners (Edeyja ts 75–80, coherence 9, `:30-31`; Orm ts 60, `:802`) at territory T15, whose
work is keeping the substrate stable — "Maintain substrate stability", "Continue the work regardless
of interference" (`:44`); "The work. Only the work." (`:811`) — by Mending at Gap margins where
environmental thread-force is high (`canon/philosophy/DECISIONS.md:425`, `06_operations.md:396`:
"Warden erosion is environmental … they Mend where environmental force is high"), at the cost of
their own Coherence, up to and including a death-Mending that seals a Gap permanently (Orm, Arc C,
`:812`). They are "the exposed … the ones who can see" (`05_confrontation_and_sensitivity.md:167`), a
"Warden zone" is a named kind of place (`07_drift.md:52`), and "the restoration of an orientation" is
"a better thing for a Warden to be doing" (`03_rendering.md:178`). Their internal structure is a
working SENIORITY — a Warden-Chief (Edeyja, `:25`) and a Second Senior Warden (Orm, `:799`, 31 years
in) — not a rank over the people they ward; they stand outside the caste and faction order and under
Church pressure (`:45`). The "dependent" they keep is the peninsula's substrate, hence everyone — and,
more narrowly, "Southernmost practitioners" (`:44`). One non-Southernmost person carries the
pursuit at 0.70 — Björn Holdar, a Varfell Jarl (`:776`) — so the pursuit is what the Wardens embody,
held by others who share it. (a) The general word, secondary: Anglo-Norman *wardein*, Germanic
*\*wardōn* "to watch, guard", cognate with "ward"/"guard" — a keeper charged with a place; the
Southernmost sense keeps exactly the "watch and keep a place" core and drops the office/rank
connotation. (b) The real-world theory, secondary and checked: STEWARDSHIP (Leopold's land ethic —
the closest fit, since the Southernmost keeps a substrate, not a person); fiduciary duty (the trustee
has no stake — fits: the Wardens gain nothing); care ethics (Gilligan's responsibility to particular
others — fits the "protect Southernmost practitioners" half, not the substrate half); Weber's
patrimonial care and *noblesse oblige* — **DO NOT FIT** and are set aside: they make wardenship a
relation of rank over dependents, which the Southernmost's structure does not have. (c) S8 §2's
"stewardship of the dependent and the vulnerable" and S1 §3.11's "protective duty of the higher-rank
to the lower (lord to peasant, steward to household)" are the generic reading; S5 `:54` restores the
row as "the only row touching the thread side", which is the Southernmost reading. Where the two
pull a cell apart, the Southernmost reading governs (§2.15 H/E).

### 1a.2 The fourteen axis poles

**hierarchical ↔ equal.** (a) Gk *hierarkhia* "rule of a high priest" (Pseudo-Dionysius's celestial
and ecclesiastical hierarchies, 5th–6th c.) — a SACRED ranked order first, any ranked order only from
the 19th c. *Aequalis* from *aequus* "level, even". (b) Weber — legitimate domination (traditional,
charismatic, legal-rational) and bureaucracy as the purest hierarchy; Michels's iron law of
oligarchy; Dumont (*Homo Hierarchicus*) — hierarchy as the encompassing of the contrary; the
disposition toward it is Sidanius & Pratto's SOCIAL DOMINANCE ORIENTATION (preference for group-based
hierarchy), the best-measured psychological construct on this axis. Equality: Tocqueville's "equality
of conditions"; Dworkin's "equality of what?"; Sen; Anderson's relational/democratic equality
(standing as equals) as against distributive equality. (c) Valoria's old `hierarchical` was
"rank-bearing, status-asserting / egalitarian, peer-levelling" (S6). ⚠ Note that "equal" here is
Anderson's RELATIONAL equality (no one ranked above), not equal TREATMENT (which is `equitable`) and
not equal DISTRIBUTION (which is a strand of `justice`). Keeping those three apart is §1b(a)'s job.

**precedent ↔ substantive.** (a) L. *praecedere* "go before"; the legal sense (a prior decision
that governs like cases, *stare decisis*) is 16th-c. *Substantia* "essence, what stands under";
"substantive" = "of the essence, actual" as against "formal/procedural". (b) Precedent: the
common-law doctrine of *stare decisis*; Burke (prescription, the wisdom of the species); Oakeshott
("Rationalism in Politics"; politics as "the pursuit of intimations" within a tradition — which
already includes changing WITHIN a tradition); Hayek (spontaneous order, inherited rules); Weber's
traditional action and traditional authority; March & Olsen's "logic of appropriateness". Substantive:
Weber's SUBSTANTIVE rationality (judging by ends and values) as against FORMAL rationality (calculable
rules); "substantive due process" vs procedural. (c) ⚠ **Valoria departs here.** Jordan's
`substantive` (S5 `:67-68`, §0.5) is "what best fits the situation without reference to the past …
forge unprecedented new ones" — this adds NOVELTY (Arendt's natality; Schumpeterian innovation;
Weber's charismatic authority, which is by definition unprecedented) to the standard sense, which is
only "on the merits rather than by form". And Jordan's `precedent` is narrower than Burkean
traditionalism: it is WHERE YOU LOOK for a resolution, not a whole disposition to conserve. Both
narrowings are what make this axis separable from `rigid ↔ flexible` (§1b(a)).

**partisan ↔ equitable.** (a) It. *partigiano* "member of a party/faction" (17th c.); *aequitas*
"evenness, fairness", which in Aristotle is *epieikeia* (*NE* V.10) — EQUITY AS THE CORRECTION OF
LAW'S GENERALITY IN THE PARTICULAR CASE, and in English law the Chancery jurisdiction that softened
common-law rigour. (b) Partisan: Schmitt (the friend/enemy distinction as the political); party
identification (Campbell et al.); Tajfel's social identity theory and in-group favouritism; Brewer.
Equitable, in the sense the axis needs: IMPARTIALITY — Barry (*Justice as Impartiality*), Nagel
(*Equality and Partiality*: the impersonal standpoint against the personal), Rawls's veil, Weber's
bureaucratic *sine ira et studio* ("without anger or fondness"), Merton's universalism. (c) ⚠ Two
hazards. First, Aristotle's *epieikeia* — equity as FLEXIBILITY of rule — is NOT what this pole
measures; if it were, Pa/Eq would collapse into R/F. The pole is read as impartiality of treatment.
Second, the pole shares a name-root with `justice`'s content; §1b(c) is where the two are kept apart.
Valoria renamed `partial` → `partisan` (S5 `:79`) only for a collision.

**selfish ↔ selfless.** (a) "Selfish" is a 17th-c. coinage (attributed to the Presbyterians, 1640s);
"selfless" 19th-c.; "altruism" coined by Comte (1851) as the antonym of egoism. (b) Hobbes
(psychological egoism); Smith (sympathy); Comte; Batson's empathy-altruism hypothesis; Sober & Wilson
(*Unto Others*); Schwartz's circumplex — SELF-ENHANCEMENT (power, achievement, hedonism) vs
SELF-TRANSCENDENCE (benevolence, universalism) is the best-measured version of this axis. The question
the axis asks is FOR WHOSE GOOD an act is done — its beneficiary. (c) S8 §2.3 had factored self/other
OUT of the convictions into `orient.self_other`; S4 folds it back as this axis and lists six pursuits
on it. S3's null finding (near-inert on the old roster) follows from S8's design, not from the axis.

**rigid ↔ flexible.** (a) L. *rigere* "to be stiff"; *flexus* "bent", *flectere* "to bend". Both
are physical words applied to persons only figuratively — ordinary-language, not technical. (b) The
nearest constructs, and they differ: Rokeach (*The Open and Closed Mind*, 1960) — DOGMATISM,
closedness of belief systems; Kruglanski — need for cognitive closure; "cognitive flexibility"
(switching between task rules); Duckworth's GRIT (perseverance of effort toward long-term goals);
Hirschman (*Exit, Voice, and Loyalty*) — loyalty as staying with a declining course; Becker's
"side-bets" theory of commitment. (c) ⚠ **Valoria's definition (§0.5) picks the PERSISTENCE family,
not the dogmatism family**: rigid = "unwilling to deviate from your course of action in the face of
difficulties" is grit/loyalty, and says nothing about openness of BELIEF. That choice is what
separates R/F from P/S (dogmatism about tradition would fuse them) and from D/I (dogmatism about
rules would fuse those). Every R/F cell in §2 must be read as persistence-of-course.

**grandiose ↔ humble.** (a) *Grandis* "great, full-grown"; "grandiose" via It. *grandioso*, an
18th-c. term of art criticism (imposing style), pejorative by the 19th c. *Humilis* "low, on the
ground", from *humus* "earth". (b) Grandiose: the clinical literature on narcissism (Kernberg,
Kohut; "grandiose vs vulnerable" narcissism), whose core is an inflated self-account relative to
others' — which is exactly CAT-9's "gap between the character's self-account and others' account of
them" (`adjudication_register.yaml:569-576`); Veblen on display; Bourdieu on distinction. Humble:
Aquinas (humility as the virtue that restrains the appetite for one's own excellence); contemporary
"intellectual humility" (Whitcomb et al.); Tangney. The question the axis asks is UNDER WHOSE GAZE an
act is done — whether it is for display. (c) Valoria took the pair from Jordan's 09-17 temperament
list ("humble ↔ vain") and `synthesis.md` §2 resolved it as *regard inverted*.

**deontological ↔ instrumental.** (a) "Deontology" coined by Bentham (*Deontology*, 1834, from Gk
*deon* "that which is binding, duty") — ironically by the founder of utilitarianism; *instrumentum*
"tool, means". (b) Deontological: Kant (the categorical imperative; duties that bind regardless of
outcome), Ross (prima facie duties, weighed case by case), Anscombe's coinage "consequentialism" for
the opponent. Instrumental: Weber's *Zweckrationalität* (means–ends rationality) vs
*Wertrationalität* (value-rationality); Horkheimer's critique of instrumental reason; Habermas. The
canonical political-theory form of this axis is Weber's "Politics as a Vocation": the ETHIC OF
CONVICTION (*Gesinnungsethik* — "the Christian does rightly and leaves the results with the Lord")
against the ETHIC OF RESPONSIBILITY (*Verantwortungsethik* — one answers for the foreseeable
consequences). (c) Jordan's definitions (S5 `:62-64`: "will not take actions they find disagreeable
even if it leads to a good outcome" / "the outcome justifies the means") are Weber's pair almost
verbatim. ⚠ Note the entailment Weber himself states: the conviction-ethicist persists WHEN THE
RESULTS ARE BAD ("if the consequences are bad, the world is to blame"), which is a form of
persistence-under-difficulty — so a theoretical correlation between D/I and R/F is expected and is
not a placement defect (§1b(a)).

---

## §1b · PHASE 2 — Comparative analysis, before any grade

### 1b(a) · Axis vs axis — do any two of the seven measure one disposition under two names?

The seven axes, each reduced to the one question Phase 1 says it asks:

| axis | the question | family |
|---|---|---|
| H/E | do I defer to rank, or level it? | social dominance orientation (Sidanius) |
| P/S | where do I look for a resolution — the past, or a new idea? | *stare decisis* / Oakeshott vs natality / charisma |
| Pa/Eq | do I treat by side, or impartially? | Tajfel vs Barry/Nagel impartiality |
| Se/Sl | for whose GOOD? | Schwartz self-enhancement vs self-transcendence |
| R/F | do I hold my course when it gets hard? | grit / Hirschman loyalty vs exit |
| G/Hu | under whose GAZE — for display, or not? | narcissistic self-account gap (CAT-9) |
| D/I | what makes an act permissible — the act, or its outcome? | Weber conviction vs responsibility |

Seven different questions. The pairs with any real risk of collapse, resolved by definition:

**P/S × R/F (rev. 2: r = +0.776).** INDEPENDENT once §0.5's narrowing is applied. P/S asks the
SOURCE of a resolution; R/F asks PERSISTENCE in it. They collapse only under the Rokeach reading of
rigidity (dogmatism), which Jordan's definition excludes, or under Burkean traditionalism, which
bundles "look to the past" AND "resist change" into one disposition — and that bundle is exactly what
S1's `traditional` column carried, so carrying that column into P/S and then reasoning R/F from the
same evidence double-counted it. The two corners Jordan named are populated in the literature:
**flexible + precedent** is Oakeshott's "pursuit of intimations" and the common law itself — when one
line of authority fails, find another; it is also Kuhn's normal science. **Rigid + substantive** is
Weber's charismatic innovator and Frankfurt's lover (a volitional necessity about a NEW object), and
Arendt's actor who begins something and stands by it. Consequence for Phase 3: R/F is placed ONLY on
persistence evidence (does the pursuit's holder keep the course under difficulty, or exit?), never
inherited from a P/S cell. **A residual positive correlation is nonetheless expected**, because
Weber's traditional authority and Hirschman's loyalty really do co-occur in some pursuits (honour,
stability), and that co-occurrence is a fact about those pursuits, not a defect of the axes.

**Se/Sl × G/Hu (rev. 2: r = +0.755).** INDEPENDENT, with an expected residual. Beneficiary vs
gaze: FOR whom vs SEEN by whom. Schwartz places both selfishness (power, achievement) and status
display inside SELF-ENHANCEMENT, so the best-measured theory predicts they co-vary across persons —
but they are not one construct, and the literature has both cross corners well populated: **selfless
+ grandiose** is Mauss's gift and the potlatch (generosity AS display), Bourdieu's honour (largesse as
symbolic capital), the conspicuous benefactor, the public martyr; **selfish + humble** is Weber's
ascetic accumulator (wealth without display), the miser, private contentment. Consequence for Phase
3: G/Hu is placed on DISPLAY evidence only; where a pursuit is theoretically a gift-economy pursuit
(honour, warden-as-hero) it may sit selfless+grandiose, and where it is a private one (wealth under
the Protestant ethic, happiness) selfish+humble. Rev. 2 had reasoned every self-side pursuit grandiose
and every other-side one humble; that was the Schwartz co-variance asserted as identity.

**R/F × D/I (rev. 2: r = +0.636).** INDEPENDENT, but the correlation is THEORETICALLY ENTAILED on
one side. Weber defines the conviction-ethicist by indifference to bad consequences — which is
persistence under difficulty by another description. So deontological pursuits WILL read rigid, and
that is Weber, not double-counting. The cross corners exist: **rigid + instrumental** is the ruthless
planner who persists ("at any cost" — Vaynard), **flexible + deontological** is Ross's prima facie
duties weighed afresh, and casuistry. Phase 3 leaves this correlation standing where a pursuit is
genuinely Weber's conviction-type and reports it as expected (§5.3).

**H/E × P/S (rev. 1: +0.735; rev. 2: +0.645).** INDEPENDENT. Weber's traditional authority couples
them (rank sanctified by the past); legal-rational authority decouples them (a hierarchy of rules
that can be new — bureaucracy is hierarchical and innovates); Tocqueville's democracy decouples the
other way (equality of conditions with a strong attachment to custom). The residual in §2 comes from
carrying S1's two columns, which co-varied in S1 (`adjudication_register.yaml:641`), and from
`liberty` (equal + substantive) being the only strong row in the off-diagonal corner.

**H/E × Pa/Eq.** INDEPENDENT. Rank vs side. Sidanius reports SDO correlates with in-group favouritism
empirically, but a hierarchy can be impartially administered (Weber's bureaucracy: *sine ira et
studio* within a strict ladder) and a levelling movement can be fiercely partisan (a revolutionary
commune). Different questions.

**Pa/Eq × Se/Sl.** INDEPENDENT. Side vs self. Brewer's in-group love is not egoism; Nagel's
"personal standpoint" includes both self and one's own, which is why they are adjacent, but a
selfless partisan (dies for the cause) and a selfish impartialist (the honest broker who takes a
fee from all sides alike) are both ordinary.

**P/S × D/I.** INDEPENDENT. Where the answer comes from vs what makes it permissible. A precedent
can be consulted instrumentally (what worked before) or deontologically (what was always done is
binding — Weber's traditional action is a THIRD type beside value-rational and instrumental). Kant's
universalisability is about rules, not the past.

**H/E × G/Hu, H/E × Se/Sl, H/E × R/F, H/E × D/I, P/S × Pa/Eq, P/S × Se/Sl, P/S × G/Hu, Pa/Eq × R/F,
Pa/Eq × G/Hu, Pa/Eq × D/I, Se/Sl × R/F, Se/Sl × D/I, R/F × G/Hu, G/Hu × D/I** — no definitional
overlap found; each pair's two questions are answerable independently for any ordinary character.
One caution only: Pa/Eq × R/F would collapse if `equitable` were read as Aristotle's *epieikeia*
(equity as bending the rule to the case); §1a fixes the pole as impartiality instead.

**Verdict on (a):** the seven are seven. Two correlations are expected by the best available theory
and are not placement defects when they appear at the magnitudes the theory predicts (Se/Sl × G/Hu
via Schwartz; R/F × D/I via Weber); one (P/S × R/F) was a genuine double-count and is resolved by
placing R/F on persistence evidence only.

### 1b(b) · Pursuit vs pursuit — are the fifteen fifteen?

| pair | distinct? | on what |
|---|---|---|
| **individuality vs liberty** | YES | Mill ch. 1 vs ch. 3: liberty is the CONDITION (non-domination, non-interference — Berlin negative, Pettit); individuality is the USE made of it (self-development — closer to Berlin's positive liberty as self-mastery). One can hold liberty without individuality (the free conformist, Mill's complaint) and individuality without liberty (the eccentric under a tyrant). They differ on H/E (liberty is anti-domination; individuality is indifferent to the ladder) and on Se/Sl (see 1b(c)) |
| **stability vs honour** (Jordan's question: honour's R/F content) | YES, but they share R/F | Stability is rigid about an ORDER (Huntington, Oakeshott: the institution persisting); honour is rigid about a personal PLEDGE (Pitt-Rivers: honour lost by yielding). Both persist; the object of persistence differs, and so do H/E (stability ruled 0; honour stratified), G/Hu (institution vs public standing) and Se/Sl. Their R/F co-occurrence is a fact about both, not a merger |
| **community vs family vs love** | YES | Tönnies's three communities — of PLACE (community), of BLOOD (family), of MIND (love, the pair) — plus Giddens's pure relationship for love and Bourdieu's reproduction strategies for family. They differ in the SCALE of the "own" (Pa/Eq magnitude), in H/E (family is a *familia* with a head; love levels its pair; community is locally flat with seniority), and in R/F (Frankfurt's volitional necessity is strongest for love) |
| **justice vs community** | YES, opposed on Pa/Eq | The liberal–communitarian debate is exactly this pair: Rawls's impartial basic structure vs Walzer's/Sandel's thick, membership-bound goods. A person can pursue both (Vossen: "Equity and social contract" AND "the community is the only legitimate political unit"), and the two rows pull her opposite ways on Pa/Eq, which is the model working |
| **virtue vs honour** | YES | MacIntyre: Homeric honour society is virtue ethics' historical predecessor; virtue INTERNALISES what honour EXTERNALISES (the excellence is its own reward vs the excellence must be acknowledged). Differ on G/Hu and on Pa/Eq (honour is owed to the pledged; virtue to all) |
| **reputation vs honour** | YES | Pitt-Rivers: honour = claim + acknowledgement; reputation (Origgi) = the acknowledgement alone, manageable strategically (Goffman). Differ on D/I (reputation can be sought instrumentally; the honour code cannot be kept instrumentally without ceasing to be honour) and on R/F |
| **wealth vs happiness** | YES | Aristotle: *chrematistics* is a MEANS, *eudaimonia* the END; the Easterlin paradox is the empirical gap. Differ on D/I (wealth-seeking is instrumental reason's paradigm; happiness is an end) — though both hedonic, both self-side |
| **happiness vs virtue** | YES **only under the hedonic reading** | Under the eudaimonic reading (flourishing = living virtuously) they are one pursuit. §1a fixes `happiness` as hedonic for this reason; Jordan should know the row's independence rests on that choice |
| **warden vs justice** | YES, opposed on Pa/Eq | Gilligan's ethic of CARE (responsibility to particular others) vs ethic of JUSTICE (impartial rights) — the canonical partial/impartial split. Warden lands partisan-and-selfless; justice equitable |
| **warden vs family** | YES | Both partial and selfless; warden's object is the SUBSTRATE and the practitioners who keep it (§1a warden: the Southernmost — a stakeless keeping, up to death-Mending), family's is the LINE (Bourdieu — reproduction of position, which is a stake). Differ on Se/Sl magnitude and on H/E (a working seniority vs a *familia* with a head) |
| **faith vs virtue / faith vs stability** | YES | Tillich's ultimate concern is about involvement, not about character (virtue) or about the order persisting (stability). Faith's affiliation-content is off the grid entirely (`Person.conviction`) |
| **scholastics vs virtue** | YES | Aristotle's intellectual virtues are virtues, but Merton's ethos (universalism, disinterestedness, scepticism) is a role-ethic for inquiry, not a character-ethic for life. Differ on P/S (the archive) and D/I |
| **stability vs precedent-the-pole** | see 1b(c) | |
| **liberty vs justice** | YES | Nozick vs Rawls is the literature: liberty (entitlement, non-interference) can conflict with distributive justice. Differ on Pa/Eq magnitude and R/F object |
| **reputation vs individuality** | YES | Origgi's second self in others' minds vs Mill's self whose desires are its own — near-opposites on G/Hu, which is why a Vaynard needs both rows to be described |

**Verdict on (b):** fifteen distinct pursuits, with two conditional independences to record —
`happiness` depends on the hedonic reading, and `stability`/`honour` genuinely share R/F content
without being one pursuit.

### 1b(c) · Pursuit vs axis-name collisions — a pursuit is an END; a pole is a disposition of TREATMENT

The general form: a pursuit is something a person is AFTER (S5 `:31` — a state of the world or of
themselves); an axis pole is a disposition about HOW they act toward anyone in getting there. Any
pursuit can be carried with any disposition (§1b(a)'s corners). So a cell is never placed by
asserting the pursuit IS the pole; it is placed by asking what the pursuit's own content does to the
disposition. Jordan's ban (§0.4) is this rule applied to one pair. The collisions:

| pursuit ↔ pole | how they differ | consequence for the cell |
|---|---|---|
| **justice ↔ equitable** | Justice is an END-STATE of institutions and distributions (Rawls's basic structure; Ulpian's *suum cuique*). `Equitable` is a disposition of TREATMENT (impartiality — Barry, Nagel). The circular placement ("justice pursues equity; equity is the pole") is banned. The INDEPENDENT argument: Rawls's justice is impartial BY CONSTRUCTION (the veil), Tyler's procedural justice is standing-blind, and Young's structural justice is claimed on behalf of all who share a position — so the pursuit's content DOES produce impartial treatment; but Walzer's spheres are community-relative, and retributive "justice for my people" (Vaynard) is partisan. Hence HIGH, not maximal — the same +0.8 rev. 2 reached, now on independent ground | +0.8 CONFIRMED |
| **liberty ↔ equal** | Berlin/Nozick: liberty and equality-of-outcome CONFLICT. But the pole is Anderson's RELATIONAL equality (no one ranked over another) and Valoria's liberty is Pettit's non-domination — which is relational equality's own content (freedom from arbitrary power = no master). So liberty lands `equal` on non-domination, NOT on any equality of distribution | +0.7 CONFIRMED |
| **individuality ↔ selfish** | Mill's individuality is not egoism (Tocqueville's *individualisme* is withdrawal, not predation; Lukes separates the strands); Schwartz puts self-direction in OPENNESS TO CHANGE, orthogonal to self-enhancement. S4 lists `individuality` on the self side (ruled), so the SIGN stands, but the theory says the magnitude was inflated | −0.7 → **−0.4** (Phase 3) |
| **community ↔ selfless** | Brewer: in-group love is not altruism; Putnam: bonding capital can be exclusionary; Durkheim's mechanical solidarity is likeness, not sacrifice. S4 lists `community` on the other side (ruled); the sign stands, the magnitude was inflated | +0.6 → **+0.4** (Phase 3) |
| **stability ↔ rigid** | Stability is the END (an order that persists); rigid is a DISPOSITION (holding one's own course). Burke: "a state without the means of some change is without the means of its conservation" — the stability-seeker may CHANGE COURSE to preserve the order (Lampedusa's "everything must change so that everything can stay the same"). Registry: Ehrenwall's "not flinching" (rigid) against Almstedt's procedural manoeuvring. So rigid, but less than rev. 2 placed | −0.5 → **−0.3** (Phase 3) |
| **honour ↔ precedent, rigid** | The code is inherited (Appiah: codes change only by moral revolutions, never by the individual shopping for another) and Pitt-Rivers: honour is LOST by yielding. Both signs are the pursuit's own content, not the pole's name | −0.8 / −0.6 CONFIRMED |
| **honour ↔ selfish** | Bourdieu's and Pitt-Rivers's honour carries OBLIGATIONS — generosity, hospitality, riposte on behalf of one's own — it is other-directed and public. S3's +0.1 selfish is contradicted by the theory; this is the selfless+grandiose corner §1b(a) said the literature populates | −0.1 → **+0.2** (Phase 3) |
| **virtue ↔ deontological** | Anscombe/Hursthouse: virtue ethics is a THIRD way; phronesis is outcome-sensitive without being calculative. S1's −0.5 read virtue as Kantian; the theory says less | −0.5 → **−0.3** (Phase 3) |
| **virtue ↔ humble** | Aristotle's *megalopsychia* (proper pride) is a virtue; Aquinas's humility is a virtue. The tradition Valoria fixes (Aristotelian) leans toward the former; rev. 2's +0.4 humble was the Christian list | +0.4 → **+0.2** (Phase 3) |
| **wealth ↔ instrumental** | Aristotle's *chrematistics* and Horkheimer's instrumental reason: wealth-seeking IS the paradigm of means–ends rationality. The pursuit's content produces the disposition | +0.6 CONFIRMED |
| **wealth ↔ grandiose** | Weber's ascetic accumulator (no display) vs Veblen's conspicuous consumer: the literature splits evenly | −0.2 → **0.0** (Phase 3) |
| **reputation ↔ grandiose** | Goffman: impression management is STRATEGIC, and a reputation for modesty is a reputation; Origgi. The pursuit implies gaze-seeking (CAT-9's gap) but not inflation of self-account | −0.6 → **−0.4** (Phase 3) |
| **individuality ↔ grandiose** | Mill's individuality needs no audience; Tocqueville's is withdrawal; only Vaynard's brand is display. Near cancel | −0.4 → **−0.1** (Phase 3) |
| **faith ↔ deontological** | Weber's illustration of the conviction ethic IS the believer. Rev. 5: Jordan's ruling makes `faith` magnitude-only; checked against his four examples, three are conviction-type, so the cell stands small | −0.3 CONFIRMED (rev. 5: stands; P/S, Se/Sl, R/F, G/Hu → 0 by the ruling) |
| **warden ↔ selfless, partisan** | §1a warden (Southernmost): the keeping is stakeless up to death-Mending (selfless); the "protect Southernmost practitioners" half is care-ethics partial, the substrate half is for everyone — net mildly partial. Both signs are the institution's own content | +0.5 / −0.3 CONFIRMED |
| **warden ↔ hierarchical** | The generic theory (Weber's patrimonial care, *noblesse oblige*, S1 §3.11's "lord to peasant") makes wardenship a RANK over dependents. §1a warden rules that reading out: the Southernmost is an independent working order with a Chief and a Second Senior, outside the caste ladder, keeping a substrate for everyone. What survives of "hierarchical" is seniority of the work | −0.5 → **−0.2** (Phase 3, on the Southernmost ruling) |
| **family ↔ partisan** | Williams's "one thought too many"; Nagel: the family is the canonical case for partiality | −0.6 CONFIRMED |
| **love ↔ selfless, partisan, rigid** | Frankfurt: disinterested concern (selfless) for THIS person (partial) as a volitional necessity (rigid — the lover cannot will otherwise). All three are the pursuit's content | +0.7 / −0.7 / −0.4 CONFIRMED |
| **liberty ↔ rigid** | Non-domination is a STATUS one holds, and the republican tradition's freeman defends it rather than negotiating it away (Skinner's neo-Roman liberty). Rev. 3's move to rigid is confirmed on the pursuit's content, not on the registry alone | −0.3 CONFIRMED |
| **individuality ↔ rigid** | Emerson's self-reliance ("nothing is at last sacred but the integrity of your own mind") and Mill's person "whose desires are his own" both describe resistance to pressure to conform — persistence of a self-authored course | −0.4 CONFIRMED |
| **scholastics ↔ precedent** | The word's own method reasons FROM authorities; Merton's organised scepticism pulls the other way. Near zero, slightly precedent | −0.1 CONFIRMED |
| **scholastics ↔ equitable** | Merton's UNIVERSALISM: claims are judged by impersonal criteria regardless of the claimant — the pursuit's content is impartial treatment of claims | +0.4 CONFIRMED |
| **stability ↔ equitable** | Weber's legal-rational authority: rule-bound, *sine ira et studio* — but a stable caste order is stable too. Moderate | +0.4 CONFIRMED |
| **happiness ↔ selfish, flexible, instrumental** | Hedonic well-being is one's own; Bentham's calculus is the instrumental paradigm; a road that stops delivering is left. All from the pursuit's (hedonic) content | −0.4 / +0.4 / +0.4 CONFIRMED |

**Verdict on (c):** nine cells change in Phase 3, all by magnitude, none by sign; every sign that a
ruling fixed (S4's six self/other placements; stability's H/E 0) stands.

---

## §2 · C1a — the 105 projection cells (PHASE 3 — graded against §1a/§1b)

**How Phase 3 is recorded.** Each pursuit's table keeps its rows; beneath each table a **Phase 3
grounding** block gives, per axis, the §1a/§1b entry the cell rests on and whether Phase 3 CONFIRMED
or CHANGED it. Where a value changed, the row itself is edited and says "CHANGED rev. 4". A
`reasoned` cell's citation is now that grounding entry first, with any corpus citation kept beneath it.

Axis columns, in `pursuit_axes` order: **H/E** hierarchical↔equal · **P/S** precedent↔substantive ·
**Pa/Eq** partisan↔equitable · **Se/Sl** selfish↔selfless · **R/F** rigid↔flexible · **G/Hu**
grandiose↔humble · **D/I** deontological↔instrumental.

### 2.1 `virtue` — was `Virtue` [+0.2, +0.4, −0.5, +0.3]; S3 `Virtue` {memory +0.1, substantive +0.4, equity +0.3, selfish +0.2}

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **−0.2** | cited | S1 §3.12 hier +0.2 — "loose hierarchy … largely peer-democratic" |
| P/S | **−0.2** | reasoned (conflict resolved) | S1 §3.12 trad +0.3 → −0.3 ("draws on ancestral exemplars but also generates new exemplars") against S3 memory +0.1 / substantive +0.4. Resolved toward S1 but smaller: the Aristotelian sense S8 §2 names is character formed by habituation on exemplars (precedent) and exercised by practical wisdom on the case (substantive) — the exemplar side is where the *pursuit* of virtue looks, so a mild precedent lean |
| Pa/Eq | **+0.3** | cited, reasoning re-grounded | S3 +0.3 kept. Substantive ground: good character is owed to whoever stands before you — the virtuous person treats stranger and kin under the same measure (treatment-under-law sense of fairness), without the distributive programme `justice` carries; hence moderate, not high |
| Se/Sl | **−0.2** | cited | S3 selfish +0.2 → −0.2; S3's null finding applies (near-inert by design) |
| R/F | **+0.2** | reasoned | no corpus citation; placed because virtue's own definition (S8 §2 "cultivation of moral character; the good life", Aristotelian) implies the mean is found *in the particular case* — a settled character applied by judgment, so the ACT bends while the disposition holds. Mild flexible |
| G/Hu | **+0.2** | reasoned — **CHANGED rev. 4** (was +0.4; §1b(c) virtue↔humble: Aristotle's *megalopsychia* is a virtue as much as Aquinas's humility, and Valoria fixes the Aristotelian tradition, so the humble lean is halved) | no corpus citation; placed because S1 §3.12's own gloss "good character is its own reward" implies the pursuit is of BEING good, not of being seen to be good — the latter is `reputation`'s row. ⚠ The nearest corpus evidence points the other way and is deliberately NOT used: Crown's Virtue framework rewards "public, visible, virtuous action" (S9 `:60`) — a faction Ob modifier, not a person's pursuit |
| D/I | **−0.3** | reasoned — **CHANGED rev. 4** (was cited −0.5; §1b(c) virtue↔deontological: Anscombe/Hursthouse — virtue ethics is a THIRD way, and *phronesis* is outcome-sensitive without being calculative; S1's −0.5 read virtue as Kantian) | corpus value beneath: S1 §3.12 instr −0.5 — "Virtue is intrinsic (good character is its own reward); strongly anti-instrumental"; lineage via S6 |

**Phase 3 grounding — virtue.** H/E: §1a virtue — the Aristotelian virtues are peer-evaluated among the free (S1's "largely peer-democratic"): CONFIRMED −0.2. P/S: §1b(a) — habituation on exemplars is a past-sourced resolution; the case is judged by *phronesis*: CONFIRMED −0.2. Pa/Eq: §1b(c) — justice is a cardinal virtue owed to all, *philia* a partial one: CONFIRMED +0.3. Se/Sl: Aristotle — the virtuous act is for *to kalon*, not for the self; no stronger ground than S3's number: CONFIRMED −0.2. R/F: §1a virtue — *phronesis* adapts the act, the disposition holds: CONFIRMED +0.2. G/Hu: §1b(c) virtue↔humble: **CHANGED +0.4 → +0.2**. D/I: §1b(c) virtue↔deontological: **CHANGED −0.5 → −0.3**.

### 2.2 `honour` — was `Honor` [+0.5, +0.4, −0.7, +0.8]; S3 `Honor` {+0.6, −0.5, −0.3, +0.1}

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **−0.5** | cited | S1 §3.13 "Honour is rank-bearing (knight's honour differs from merchant's…)" |
| P/S | **−0.8** | cited | S1 §3.13 trad +0.8 "honour codes are ancestral and slow-moving … Honour's primary axis is traditional"; S3 corroborates (memory +0.6, substantive −0.5) |
| Pa/Eq | **−0.3** | cited, reasoning re-grounded | S3 −0.3 kept. Substantive ground: honour binds to the PLEDGED party — oath, liege, comrade — and its obligations do not run to the unpledged; against a standing-blind rule it is partial by construction (Virke: "your word is your network", S7 `:256`). Moderate, because the code itself is applied consistently to whoever is inside it |
| Se/Sl | **+0.2** | reasoned — **CHANGED rev. 4** (was cited −0.1; §1b(c) honour↔selfish: Bourdieu's and Pitt-Rivers's honour carries OBLIGATIONS — generosity, hospitality, riposte on behalf of one's own — other-directed; this is §1b(a)'s selfless+grandiose corner) | corpus value beneath: S3 selfish +0.1, with its own null-finding caveat |
| R/F | **−0.6** | derived — **re-examined rev. 3, KEPT** | direction from S1 §3.13 "one keeps the oath even at material cost … slow-moving"; magnitude mine. Under §0.5's test: honour is "hold to THIS pledged code in the face of difficulty", not "try a different old code when this one is hard" — the oath-keeper at material cost is rigid by Jordan's definition, and precedent by where the code comes from. Both signs stand on the same evidence; no registry row reads otherwise (Haldorsen "Completes missions Sigrid aborts", S7 `:829`; Virke "your word is your network", `:256`) |
| G/Hu | **−0.4** | reasoned | no corpus citation; placed because honour's definition (S8 §2 "pledged oath, honor-code") implies standing AMONG PEERS — an oath is sworn before witnesses, an affront must be answered where it was given — so the pursuit has a public face even after ED-IN-0261 split `reputation` off (§2.6 carries the reputational half; this cell carries only the witnessed-code half, hence −0.4 not −0.6) |
| D/I | **−0.7** | cited | S1 §3.13 "the *anti-instrumental* Conviction" |

**Phase 3 grounding — honour.** H/E: §1a honour — stratified (Pitt-Rivers; Weber's *ständische Ehre*): CONFIRMED −0.5. P/S: §1b(c) honour↔precedent — Appiah: the code is inherited: CONFIRMED −0.8. Pa/Eq: §1a honour — obligations run to the pledged: CONFIRMED −0.3. Se/Sl: §1b(c) honour↔selfish: **CHANGED −0.1 → +0.2**. R/F: §1b(c) — Pitt-Rivers: honour is lost by yielding: CONFIRMED −0.6. G/Hu: §1a honour — challenge-and-riposte is public by construction; with Se/Sl now +0.2 this row occupies §1b(a)'s selfless+grandiose corner: CONFIRMED −0.4. D/I: §1a — the code binds regardless of outcome (Weber's conviction ethic): CONFIRMED −0.7.

### 2.3 `liberty` — was `Liberty` [−0.7, −0.2, +0.1, −0.5]; S3 `Liberty` {−0.3, +0.2, +0.3, +0.1}

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **+0.7** | cited | S1 §3.7 "*Libertas* = freedom from imposed authority. Strongly egalitarian" |
| P/S | **+0.5** | cited | S1 §3.7 trad −0.5 "rejects ancestral imposition"; S3 corroborates (memory −0.3, substantive +0.2) |
| Pa/Eq | **+0.2** | reasoned (was S3 +0.3; **changed by the equity correction**, §7.3) | Substantive ground: liberty is freedom from IMPOSED authority (S1 §3.7) — a claim about structural outcomes (nobody placed under another by station), which is the structural-equity strand of social justice; but it carries no distributive programme and, in its period sense, is the CITIZEN body's freedom (Grindvold "defends guild autonomy", S7 `:904`; Vedel copies suppressed texts for the Einhir, `:949`) — partial to those inside the claim. Lenneth links the two explicitly: "Caste suppression is wrong … political self-determination follows" (`:448`). Net mild equitable, lower than S3's number |
| Se/Sl | **−0.1** | cited | S3 selfish +0.1; S4 does not list `liberty` on either side of self/other |
| R/F | **−0.3** | reasoned — **MOVED rev. 3** (was +0.4) | Rev. 2 argued "the person who will not be bound chooses afresh" — that is a P/S argument (a new arrangement), not an R/F one, and §0.5's test separates them. Re-read against the registry: the liberty-pursuers HOLD their new claim when it gets hard — Vedel "each copy takes weeks, possession is a heresy charge, no press to seize" and copies anyway (S7 `:949`); Vaynard "Einhir cultural revival AT ANY COST" (`:715`); Lenneth pursues "caste dismantlement through royal decree" into a Widow-Regent arc (`:449-450`); Grindvold "defends guild autonomy against Crown regulation" as a standing brief (`:904`). None goes shopping for a different arrangement when the first is resisted. That is Jordan's rigid+substantive corner ("will refuse to deviate from their new idea"). Moderate rigid; not strong because Ehrenwall's Liberty .20 is written as a FALLBACK course ("if Order fails…", S9 `:141`), which is deviation. P/S stays +0.5 |
| G/Hu | **0.0** | reasoned | no corpus citation; placed at zero because self-determination says nothing about display — it is claimed loudly (Vaynard) or quietly (Vedel's hand-copying) with equal fit. A reasoned zero, not an unplaced cell |
| D/I | **+0.1** | cited | S1 §3.7 "principled but calculates means to defend itself. Near-zero" |

**Phase 3 grounding — liberty.** H/E: §1b(c) liberty↔equal — non-domination IS relational equality's content: CONFIRMED +0.7. P/S: §1a liberty — Constant's modern liberty against ancestral imposition: CONFIRMED +0.5. Pa/Eq: §1b(c) — non-domination is a common good of the citizen body, which is bounded: CONFIRMED +0.2. Se/Sl: Pettit — one's own freedom and others' are the same status: CONFIRMED −0.1. R/F: §1b(c) liberty↔rigid — the neo-Roman freeman defends his status rather than negotiating it: CONFIRMED −0.3 (rev. 3's move, now on the pursuit's content). G/Hu: §1a — Constant's modern liberty is private, the ancients' public: CONFIRMED 0.0. D/I: §1a — Berlin's liberty is held for itself but defended by calculation: CONFIRMED +0.1.

### 2.4 `justice` — was null. Nearest OLD row: `Equity` [−0.4, +0.2, −0.2, −0.2]; S3 `Equity` {−0.3, +0.6, +0.9, −0.2} — ANALOGY, not lineage

Why `Equity` and not nothing: `PROPOSAL.md:660` calls `Equity` an orphan, but every `Equity`-weighted
person in S7 is written as a justice-seeker — Lenneth "Caste suppression is wrong (Equity)" (`:448`),
Vossen "Equity and social contract" (`:93`), Vaynard "Einhir revival idealism (Equity)" (`:628`), Uln,
Orm, Askeland, Vedel — and S8 §2 defines Equity as "fairness across station; **relief of injustice**".
⚠ The counter-reading exists and is Jordan's own canon: Baralta, "Constitutional **procedure IS
justice**" (S9 `:99`), is a PRECEDENT-justice person. Both flavours are one pursuit separated by the
P/S axis of their OTHER pursuits — which is what the row below tries to allow by staying near 0 on P/S.

**What "justice" means in these cells (rev. 2, per Jordan's rule).** Not the axis label. The
substantive concept is **social justice**: (a) *distributive fairness* — who gets what, and whether
station decides it (caste, tithe, guild share); (b) *treatment under law* — the same procedure for
whoever stands before it (Baralta's strand); (c) *structural equity in outcomes* — correcting an
entrenched disadvantage rather than only a single wrong (Lenneth's "caste dismantlement through royal
decree", Vossen's "social contract"). A person pursuing justice is after (a), (b) or (c) being DONE in
the world; the cells below are placed on that, and S3's `equity` column is cited only where it
corroborates.

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **+0.4** | analogy, reasoning re-grounded | S1 §3.6 "argues *against* unjust hierarchy but does not deny rank entirely". Substantive ground: strands (a) and (c) are claims that station should not decide outcomes — the caste order is the structure Lenneth's and Vossen's justice is aimed at — while strand (b) leaves rank standing and asks only that the rule bind it too. Net moderate `equal` |
| P/S | **+0.1** | reasoned (conflict resolved) | S1 §3.6 trad −0.2 → +0.2 and S3 substantive +0.6 say substantive; Baralta (S9 `:99`, strand b) says precedent. Resolved to a small positive: strands (a) and (c) judge the outcome in front of them against what SHOULD be, which is substantive by Jordan's definition (S5 `:67-68`); strand (b) consults what was established. Two of three strands lean substantive; the third is real and keeps the value near zero |
| Pa/Eq | **+0.8** | reasoned (was S3-analogy +0.9; **changed by the equity correction**, §7.3) | Substantive ground: all three strands are the same demand — that who a person IS (side, station, kin) should not decide what they get or how the rule treats them — which is the `equitable` pole's content stated independently of its name. Reduced from S3's 0.9 because one live flavour of the pursuit is partisan: "justice for MY people" — Vaynard's "Einhir cultural revival at any cost" (S7 `:715`), Torberg's "Fights for Einhir" (`:859`) — where the wrong to be righted is one side's. High, not maximal |
| Se/Sl | **+0.2** | analogy | S3 selfish −0.2 |
| R/F | **−0.3** | reasoned — not among rev. 3's 11 (P/S and R/F already opposite-signed); noted as one of the rigid+substantive corner's occupants | no corpus citation; placed because a standard of desert or of procedure, once held, is not traded for the convenient outcome — the pursuit's whole content is that the right result is owed whatever the case's pressures (Baralta "unshakeable force of conviction", S7 `:690`). Moderate rigid |
| G/Hu | **0.0** | reasoned | no corpus citation; placed at zero because justice is pursued as a public cause (Vossen, "visibility as vulnerability", `:92`) and as a clerk's quiet correction (Almstedt) with equal fit — the pursuit does not choose a display. A reasoned zero |
| D/I | **−0.2** | analogy | S1 §3.6 "principled (fairness as principle) rather than calculative" |

**Phase 3 grounding — justice.** H/E: §1a justice — Rawls's difference principle and Anderson's relational equality against station: CONFIRMED +0.4. P/S: Rawls/Sen judge the arrangement on its merits (substantive); Tyler's procedural strand looks to established procedure: CONFIRMED +0.1. Pa/Eq: §1b(c) justice↔equitable — impartial by construction (the veil), partial in the retributive flavour: CONFIRMED +0.8. Se/Sl: the original position abstracts from self; Nozick's entitlement protects one's own: CONFIRMED +0.2. R/F: *fiat iustitia ruat caelum* — the standard is not traded: CONFIRMED −0.3. G/Hu: no lean in the literature: CONFIRMED 0.0. D/I: Rawls — the right is prior to the good (deontological) against utilitarian justice: CONFIRMED −0.2.

### 2.5 `wealth` — was null

⚠ **A superseded ruling bears on this row and is recorded rather than hidden.** S8 §2.3: *"Greed,
ambition, and self-aggrandizement are not Convictions in this taxonomy. They are represented via
Self-Other orientation."* ED-IN-0261 (S4) reverses that by making `wealth` a pursuit and dropping
`Person.orient`. The nearest OLD evidence is not a row but three people and one faction framework:
Feldhaus (`Utility 0.50`, goals "Maximize Guilds Wealth", "PROFIT-MAXIMISING", S7 `:183-189`), Virke
("Maintain Virke trade network", `:257`), Tormann ("Maximize Church Wealth throughput", `:327`), and the
Guilds' framework "Moral Relativism … +1 Ob on actions requiring moral consistency" (S9 `:263`). All are
`Utility` carriers, so `Utility` [−0.1, −0.5, +0.9, −0.4] / S3 {−0.7, +0.9, 0.0, 0.0} is the analogy row.

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **−0.2** | reasoned | no corpus citation for the pursuit; placed because in Valoria wealth is a road INTO the ranked order — `proposals/2026-08-30-fixes/05_the_blocked_cores.md:547` records that `found` "gives the design a way for material wealth to become political standing" — so the pursuit of wealth is mildly the pursuit of a higher place, not of levelling. Small, because S1 §3.5's Utility "ignores rank if rank impedes outcomes" pulls the other way |
| P/S | **+0.4** | analogy | S1 §3.5 trad −0.4 "breaks tradition when tradition impedes outcomes"; S3 Utility memory −0.7 / substantive +0.9. Magnitude = S1's |
| Pa/Eq | **−0.4** | reasoned | no corpus citation on the axis; placed because the pursuit of wealth is the pursuit of ONE'S OWN share, and distributive fairness is exactly what it trades against — the registry writes the trade in both directions: Feldhaus "sacrifices Guilds Mandate for Wealth" (S7 `:189`) and Kessler "Pushes Mandate over Wealth" as her opponent (`:889`). Moderate partisan; not high, because wealth-seeking under a fair rule (honest trade) is common |
| Se/Sl | **−0.6** | derived | **S4 rules the direction**: "self/other lives in the pursuit space (wealth, reputation, individuality against community, family, love)". Magnitude mine |
| R/F | **+0.5** | reasoned — **re-examined rev. 3, KEPT** | no corpus citation for the pursuit; placed because wealth-seeking takes whichever road pays — the nearest text is the Guilds' framework "+1 Ob on actions requiring moral consistency" (S9 `:263`), a faction modifier used here as an analogy for the disposition, not as a citation. Under §0.5's test: the wealth-seeker changes ROUTE when a route is blocked while holding the GOAL — Feldhaus "sacrifices Guilds Mandate for Wealth" (S7 `:189`) is a deviation of course in the face of difficulty, which is Jordan's flexible. The one counter-instance, Tormann's "aggressive tithe collection" driven into a Parish Revolt arc (`:327-328`), is a man who does not deviate — real, and why this is +0.5 rather than higher. Kept |
| G/Hu | **0.0** | reasoned — **CHANGED rev. 4** (was −0.2; §1b(c) wealth↔grandiose: Weber's ascetic accumulator against Veblen's conspicuous consumer — the literature splits evenly, so a reasoned zero) | no corpus citation; rev. 2 placed −0.2 because wealth displayed is standing (the same reasoning as H/E) but wealth hoarded is quiet — the pursuit does not require an audience the way `reputation` does. Slight grandiose |
| D/I | **+0.6** | analogy | Feldhaus "greatest good for greatest number of guild members" (S7 `:187`); Utility instr +0.9 (S1 §3.5); magnitude reduced because wealth-seeking is narrower than Utility |

**Phase 3 grounding — wealth.** H/E: §1a wealth — Bourdieu's conversion of economic into symbolic capital; Weber's class/status: CONFIRMED −0.2. P/S: *chrematistics* is unlimited acquisition by whatever new means (Schumpeter's entrepreneur): CONFIRMED +0.4. Pa/Eq: acquisition is of one's own share: CONFIRMED −0.4. Se/Sl: S4 + Schwartz self-enhancement: CONFIRMED −0.6. R/F: §1a rigid/flexible — Hirschman's EXIT is the market disposition: CONFIRMED +0.5. G/Hu: §1b(c) wealth↔grandiose: **CHANGED −0.2 → 0.0**. D/I: §1b(c) wealth↔instrumental — Horkheimer's paradigm: CONFIRMED +0.6.

### 2.6 `reputation` — was null (renamed from `status`, S5 `:35`, S4)

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **−0.3** | reasoned | no corpus citation; placed because reputation is standing in others' eyes and standing in Valoria is RANKED — `title_rank` reads "higher governs wider" (`data/rosters.py`, cited at `decision_layer_v1.md:178`), caste marks a person's place — so the pursuit of reputation is the pursuit of a higher rung in the eyes that count. Moderate hierarchical |
| P/S | **−0.2** | reasoned | no corpus citation; placed because reputation is earned against what has ALREADY been esteemed — one is reputed by the standards others hold from before, so the pursuit looks to established expectation. Mild precedent |
| Pa/Eq | **−0.3** | reasoned | no corpus citation on the axis; placed because reputation is with an AUDIENCE — the regard of those whose regard counts (Strand's court, Virke's network) — and it is cultivated toward them, not toward whoever stands before you; fair treatment of the unregarded buys nothing. Moderate partisan |
| Se/Sl | **−0.6** | derived | S4: on the self side of the pursuit space. Magnitude mine |
| R/F | **+0.3** | reasoned | no corpus citation; placed because reputation-seeking bends to its audience — Strand's flattery vulnerability (S7 `:235`) and CAT-9's "insecure … high gain on incoming claims" (`adjudication_register.yaml:577-582`) are the same shape: the reputed adjust to how they are read. Moderate flexible |
| G/Hu | **−0.4** | derived — **CHANGED rev. 4** (was −0.6; §1b(c) reputation↔grandiose: Goffman's impression management is strategic and a reputation for modesty is a reputation; gaze-seeking yes, inflated self-account not necessarily) | `synthesis.md` §2 / CAT-9 (`adjudication_register.yaml:569-576`): humble↔vain is "the gap between the character's self-account and others' account"; the pursuit of reputation is the pursuit of the others'-account, and S4 chose `reputation` precisely as `standing_of`'s "CONTRASTING concept" (`options.py:477`). Magnitude mine |
| D/I | **+0.3** | reasoned | no corpus citation; placed because an act chosen for how it will be SEEN is chosen for its effect, which is Jordan's `instrumental` ("the outcome justifies the means", S5 `:64`) — tempered because a reputation for keeping one's word is bought only by principled acts. Honour's −0.7 is not carried: S4 split reputation off honour rather than out of it |

**Phase 3 grounding — reputation.** H/E: §1a reputation — Weber's status honour is a rank: CONFIRMED −0.3. P/S: Ridgeway — one is reputed against established expectation: CONFIRMED −0.2. Pa/Eq: Origgi — reputation is audience-specific: CONFIRMED −0.3. Se/Sl: Schwartz achievement/self-enhancement: CONFIRMED −0.6. R/F: Goffman — impression management is adaptive: CONFIRMED +0.3. G/Hu: §1b(c) reputation↔grandiose: **CHANGED −0.6 → −0.4**. D/I: Goffman — strategic: CONFIRMED +0.3.

### 2.7 `scholastics` — was `Scholastic` [+0.1, +0.2, +0.3, −0.1]; S3 `Scholastic` {+0.2, −0.5, +0.4, 0.0}

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **−0.1** | cited | S1 §3.4 "respects intellectual rank … largely peer-evaluative" |
| P/S | **−0.1** | reasoned (conflict resolved) | S1 §3.4 trad −0.1 ("also generates *new* knowledge") against S3 memory +0.2 / substantive −0.5 (the method as commentary on authorities). Resolved to a small NEGATIVE, reversing rev. 1's S1 primary: by Jordan's definition (S5 `:65`) precedent is *where you look for the answer*, and the scholastic looks to the archive first — the registry's scholastics are archive and record readers (Klapp "TS exposure via archive work" `:621`, Bergvall the surveyor `:919`, Grindvold "Evidence" style) — while the FINDING may be new. The method is precedent-bound; the pursuit is of the method |
| Pa/Eq | **+0.4** | cited, reasoning re-grounded | S3 +0.4 kept. Substantive ground: evidence is no respecter of persons — a finding holds for whoever stands before it, and the scholar's standard is applied to the claim, not to the claimant (Bergvall's data "undermines Varfell conspiracy narrative" regardless of side, `:919`). Treatment-under-a-rule sense of fairness; no distributive content, so moderate |
| Se/Sl | **0.0** | cited | S3 selfish 0.0 |
| R/F | **+0.3** | reasoned | no corpus citation; placed because inquiry revises on evidence by definition — the scholar who cannot change a conclusion is not pursuing scholastics (Bergvall's finding overturns a narrative, `:919`). Moderate flexible |
| G/Hu | **+0.2** | reasoned | no corpus citation; placed because the pursuit defers to evidence and to authorities over the self — Klapp's "Scholar's Dilemma" (`:621`) is a person whose findings endanger his standing and who pursues them anyway. Mild humble |
| D/I | **+0.3** | cited | S1 §3.4 "reasoned inquiry is *means* to truth" |

**Phase 3 grounding — scholastics.** H/E: Bourdieu's academic field is ranked but peer-evaluative: CONFIRMED −0.1. P/S: §1b(c) scholastics↔precedent — the method reasons from authorities; Merton's scepticism pulls back: CONFIRMED −0.1. Pa/Eq: §1b(c) — Merton's universalism: CONFIRMED +0.4. Se/Sl: Merton's disinterestedness: CONFIRMED 0.0. R/F: Merton's organised scepticism revises on evidence: CONFIRMED +0.3. G/Hu: Merton's "communism" — findings are not one's own: CONFIRMED +0.2. D/I: inquiry as means to truth (S1), against Weber's science as a value-rational vocation: CONFIRMED +0.3.

### 2.8 `stability` — was null; nearest `Order` [+0.5, −0.1, +0.2, +0.4] (S5 `:114`: "NOT the same pursuit"); `Authority` also folds here (S5 `:47`); S3 `Order` {+0.2, −0.9, +0.4, 0.0}

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **0.0** | **cited (ruled)** | S4: "`stability` also fixes an independence problem `authority` had: you can want a stable EQUAL society, so it is orthogonal to hierarchical/equal". ⚠ This DEPARTS from Order's +0.5 and Authority's +0.9 on purpose |
| P/S | **−0.4** | analogy | S1 §3.3 trad +0.4 "procedures derive from past practice"; S3 Order substantive −0.9 (strongly procedural); Ehrenwall "Order is not made — it is maintained" (S9 `:58`). Magnitude = S1's |
| Pa/Eq | **+0.4** | analogy, reasoning re-grounded | S3 Order +0.4 kept. Substantive ground: a stable order is one whose rule binds whoever stands before it — the treatment-under-law strand (Baralta's "constitutional framework supersedes Church jurisdiction", S7 `:691`; Haelgrund's "Administrative Proceduralism", S9 `:313`) — with no distributive claim; a stable CASTE order is also stable, which is why this is moderate and not high |
| Se/Sl | **0.0** | analogy | S3 Order selfish 0.0; S4 lists `stability` on neither side |
| R/F | **−0.3** | derived — **CHANGED rev. 4** (was −0.5, kept in rev. 3; §1b(c) stability↔rigid: stability is the END, rigid the disposition — Burke's "a state without the means of some change is without the means of its conservation"; the stability-seeker may change course to keep the order, as Almstedt manoeuvres where Ehrenwall does not flinch) | S8 §2 Order = "rule-following, institutional regularity"; Almstedt "CONSERVATIVE — blocks radical action through procedure" (S7 `:175`); Ehrenwall "Everything depends on not flinching" (S9 `:58`). Magnitude mine. Under §0.5's test: stability's whole content is not deviating from the established course under pressure — "not flinching" is Jordan's rigid verbatim — and the course comes from past practice (P/S −0.4). The two signs rest on different sentences of the same evidence, not on one read twice. Kept |
| G/Hu | **+0.2** | reasoned | no corpus citation; placed because stability seeks the INSTITUTION's continuance over the person's prominence — Haelgrund "The work continues regardless of who sits on the throne" (S9 `:311`), Almstedt blocking "through procedure, not force" (S7 `:175`). Mild humble; mild because a stability-seeker can also be the visible pillar (Ehrenwall) |
| D/I | **+0.2** | analogy | S1 §3.3 "means-to-ends thinking applied to institutional regularity. Mild" |

**Phase 3 grounding — stability.** H/E: S4 ruled + §1a stability — Huntington: order is prior to its form: CONFIRMED 0.0. P/S: Oakeshott's disposition to prefer the tried: CONFIRMED −0.4. Pa/Eq: §1b(c) stability↔equitable — Weber's rule-bound impersonality, but a caste order is stable too: CONFIRMED +0.4. Se/Sl: no lean: CONFIRMED 0.0. R/F: §1b(c) stability↔rigid: **CHANGED −0.5 → −0.3** (Burke's means of change). G/Hu: institution over person (Haelgrund): CONFIRMED +0.2. D/I: Weber's formal rationality is instrumental in form: CONFIRMED +0.2.

### 2.9 `individuality` — was null

Nothing in the corpus describes this pursuit beyond its name in S4. `Identity` (old) is its
categorical OPPOSITE (S8 §2.1 "membership in a categorical group"), not an analogy; `Liberty` is
political freedom, not selfhood. **Working definition used for the reasoned cells:** the pursuit of
being, and being taken as, a distinct self — not defined by station, side, kin or precedent. Vaynard
is the registry's nearest instance ("ego-driven, wants to be THE ONE who tears down the order", S7
`:628`), and §4.3 migrates his orphaned `Utility .30` here.

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **+0.3** | reasoned | no corpus citation; placed because a self that refuses to be defined by station refuses the ladder's claim on it — but does not thereby level others (an individualist may want to rise). Mild `equal`, for the refusal of placement rather than for any egalitarian programme |
| P/S | **+0.5** | reasoned | no corpus citation; placed because judging by one's own lights rather than by what was done before is the definition's core — the most substantive pursuit on the grid by Jordan's own gloss (S5 `:67-68` "what they think best fits the situation without reference to the past") |
| Pa/Eq | **−0.2** | reasoned (**new cell under the equity correction**, §7.3) | Substantive ground: the pursuit is indifferent to distributive fairness and to treatment-under-law alike — it is for ONESELF, the smallest possible "own side". On an axis whose negative pole is *for one's own*, that is mildly partisan, not equitable; mild because indifference is not opposition |
| Se/Sl | **−0.4** | derived — **CHANGED rev. 4** (was −0.7; §1b(c) individuality↔selfish: Mill's individuality is not egoism and Schwartz's self-direction sits in openness-to-change, not self-enhancement; S4's ruling keeps the SIGN, the theory shrinks the magnitude) | S4: self side. Magnitude: rev. 2 placed it as the most self-directed of the three because it names the self; §1a says the name misleads |
| R/F | **−0.4** | reasoned — **MOVED rev. 3** (was +0.3) | Rev. 2's "it can be re-authored" was speculation against the row's own evidence, and its final clause ("the individualist's own line, once drawn, is held") already contained the correction. Re-read against the registry: Vaynard, the nearest instance, is the "Von Lohengramm programme — revolutionary expulsion" (S7 `:630`), a self-authored course held so stubbornly that Torberg's fracture line is "if Vaynard's ego diverges from cause" (`:859`) — the ego does not bend, the alliance does. That is §0.5's rigid+substantive corner exactly: "invented your own answer, now won't budge from it". Moderate-strong rigid. P/S stays +0.5 |
| G/Hu | **−0.1** | reasoned — **CHANGED rev. 4** (was −0.4; §1b(c) individuality↔grandiose: Mill's individuality needs no audience and Tocqueville's *individualisme* is withdrawal; only Vaynard's brand is display — near cancel) | no corpus citation; rev. 2 placed −0.4 because being DISTINCT is partly being SEEN to be distinct — Vaynard's "wants to be the one who tears down the order" (S7 `:628`) is display as much as deed. Moderate grandiose |
| D/I | **0.0** | reasoned | no corpus citation; placed at zero because individuality fixes WHOSE line governs (mine), not whether there is an inviolable line at all — an individualist's "I will not" is deontological and an individualist's "whatever gets me there" is instrumental with equal fit. A reasoned zero |

**Phase 3 grounding — individuality.** H/E: §1a individuality — Mill against custom's tyranny, not against rank as such: CONFIRMED +0.3. P/S: Mill ch. 3 — desires that are one's own: CONFIRMED +0.5. Pa/Eq: indifferent to both strands of fair treatment; the smallest own side: CONFIRMED −0.2. Se/Sl: §1b(c) individuality↔selfish: **CHANGED −0.7 → −0.4**. R/F: §1b(c) individuality↔rigid — Emerson, Mill against conformity pressure: CONFIRMED −0.4 (rev. 3's move, now on the pursuit's content). G/Hu: §1b(c) individuality↔grandiose: **CHANGED −0.4 → −0.1**. D/I: fixes whose line, not whether there is one: CONFIRMED 0.0.

### 2.10 `community` — was `Community` [0.0, +0.3, −0.2, +0.5]; S3 `Community` {+0.3, +0.3, −0.5, −0.2}

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **0.0** | cited | S1 §3.9 "locally egalitarian (parish) but with internal seniority. Near-zero". ⚠ Vossen's "power must flow from the people" (S9 `:161`) argues `equal`, but her old primary is `Equity`, so it is §2.4's evidence, not this row's |
| P/S | **−0.5** | cited (mild conflict) | S1 §3.9 trad +0.5 "*we have always been here*"; S3 is mixed (memory +0.3, substantive +0.3). Primary = S1 |
| Pa/Eq | **−0.3** | reasoned (was S3 −0.5; **changed by the equity correction**, §7.3) | Substantive ground: community has TWO relations to fair treatment. Inside the circle, distributive fairness is its content — the commons, mutual aid, "actions benefiting common population" (S9 `:163`), Kessler the "communal advocate" (S7 `:889`), Falkenrath the "commune voice against city power-politics" (`:844`). At the boundary it is partial: the outsider is not owed the common life. The registry's community-pursuers are the peninsula's fairness advocates, so the net partiality is smaller than S3's −0.5 |
| Se/Sl | **+0.4** | derived — **CHANGED rev. 4** (was +0.6; §1b(c) community↔selfless: Brewer's in-group love is not altruism, Putnam's bonding capital can exclude, Durkheim's mechanical solidarity is likeness not sacrifice; S4's ruling keeps the SIGN) | S4: other side; S3 selfish −0.2 corroborates the sign. Magnitude mine |
| R/F | **−0.2** | reasoned — **re-examined rev. 3, KEPT** | no corpus citation; placed because common life runs on shared custom and expectation — the community-member does what is done here — so a mild rigid; mild because a commune also deliberates (Falkenrath's Diet-of-Stans mediation, `:844`). Under §0.5's test the registry splits: Kessler "Pushes Mandate over Wealth" against Feldhaus and does not yield (`:889`, rigid); Falkenrath mediates (flexible); Askeland runs an illegal hedge school under discovery risk (`:934`, rigid). Net mild rigid; its contribution to the correlation was small (|−0.2|) and no evidence moves it. Kept |
| G/Hu | **+0.4** | reasoned | no corpus citation; placed because belonging subordinates the self to the common life by definition (S8 §2 "belonging to the immediate community; common life") — the "commune voice", not the individual's. Moderate humble |
| D/I | **−0.2** | cited | S1 §3.9 "intrinsically motivated (belonging-as-good); mild anti-instrumental" |

**Phase 3 grounding — community.** H/E: §1a community — Tönnies's community of place has seniority; Turner's *communitas* levels: CONFIRMED 0.0. P/S: Tönnies's natural will and custom: CONFIRMED −0.5. Pa/Eq: §1b(b) justice vs community; Putnam's bonding vs bridging: CONFIRMED −0.3. Se/Sl: §1b(c) community↔selfless: **CHANGED +0.6 → +0.4**. R/F: custom, mild; a commune deliberates: CONFIRMED −0.2. G/Hu: Durkheim — the individual subordinate to the collective: CONFIRMED +0.4. D/I: belonging as a good in itself (Sandel): CONFIRMED −0.2.

### 2.11 `faith` — was `Faith` [+0.4, +0.9, −0.3, +0.6]; S3 `Faith` {+0.4, −0.3, +0.2, −0.1}

⚠ **This is the row the whole placement is tested on (H7), and the `was:` values cannot be carried
as they stand.** Old `Faith` is S8 §2's "devotion to **ecclesiastical** authority and theological
order" — the orthodox side. The new `faith` is "how much of yourself goes into religious matters at
all" (S5 `:124-126`), which side being `Person.conviction`'s. S1 §3.1's own rationale for `hier +0.4`
is *"places one within an ecclesiastical order (Pope → Cardinals → …)"* — that is the affiliation's
hierarchy, which R1/R2 moved off this basis. Carrying it would pull Jordan's Einhir dismantler toward
the Church's hierarchy in proportion to his faith, which is the ED-IN-0214 defect by construction.
§5 arm D measures exactly that: with the `was:` row carried, the pair FAILS (cos 0.708).

**RULED 2026-09-27 (Jordan, via the coordinator), and enacted in rev. 5.** Verbatim: *"faith would
just be someone's orientation towards pursuing actions/decisions that concern faith, be it agnostic
pursuit of Truth, a Solmund zealot doing things that respect the religious tenets, an atheist trying
to shut down or discredit religions, or an Einhir revivalist pursuing its revival."* So `faith` is the
MAGNITUDE of a person's orientation toward religious matters — how much of their action and
decision-making concerns it at all — and not the DIRECTION of that concern (which side, how
intensely: `Person.conviction`, R1/R2) nor the DISPOSITION with which it is pursued (rigid or
flexible in HOW, humble or grandiose in HOW displayed: carried by whatever OTHER pursuits the person
holds — a Solmund zealot's rigidity, if real, shows on `virtue`/`honour`/`stability`'s own R/F cells,
not on `faith`'s). Applied to each cell below: a cell keeps a non-zero value only if it holds for ALL
FOUR of Jordan's examples; where the four split, the cell is 0.

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **0.0** | cited (ruled) | already 0 in rev. 2 for the same reason the ruling makes general: S1 §3.1's +0.4 is the ecclesiastical ladder, which is the zealot's direction, not the atheist's or the agnostic's — a DIRECTION, now `Person.conviction`'s. Confirmed by the ruling |
| P/S | **0.0** | cited (RULED, 2026-09-27) — **CHANGED rev. 5** (was derived −0.3) | The four examples split 2/2: the zealot returns to the tenets and the revivalist to a past (precedent); the agnostic pursuing Truth and the atheist discrediting religion forge their own resolution (substantive). A cell that holds for two of four is a direction, not the magnitude — 0. (S1 §3.1's trad +0.6, "grounded in scripture and tradition", was the zealot's reading only) |
| Pa/Eq | **+0.2** | cited, reasoning re-grounded — **STANDS (outside the instruction; see the flag below)** | S3 +0.2 kept. Substantive ground: all four examples make a claim about how EVERYONE stands to the matter — the zealot's tenets bind all, the atheist wants religion discredited for all, the agnostic's Truth is one truth, the revivalist's revival is a people's — which is a treatment-under-one-rule shape common to the four; each also has an inside and an outside, hence mild |
| Se/Sl | **0.0** | cited (RULED, 2026-09-27) — **CHANGED rev. 5** (was derived +0.3) | Rev. 2's "self given over" (S5 `:124-126`) held for the zealot and the revivalist; the agnostic's pursuit of Truth is their own understanding and the atheist's campaign may be for themselves or for others — the four split. Jordan's formulation is about SUBJECT MATTER ("actions/decisions that concern faith"), not self-giving, so the magnitude carries no beneficiary — 0 |
| R/F | **0.0** | cited (RULED, 2026-09-27) — **CHANGED rev. 5** (was reasoned −0.4) | Ruled: `faith` is not the disposition. Rev. 2 placed −0.4 because "devotion of either side holds its tenets against circumstance" (Himlensendt's "load-bearing wall", S10 `:608`; "PURE Einhir", S5 `:128`) — that is the zealot's and the revivalist's rigidity, which their OTHER pursuits carry (§1b(c) honour↔rigid, stability↔rigid, liberty↔rigid); the agnostic revises on evidence. §5.2 arm E had isolated this cell and G/Hu as the two that made the pair fail |
| G/Hu | **0.0** | cited (RULED, 2026-09-27) — **CHANGED rev. 5** (was reasoned +0.3) | Ruled: `faith` is not how it is displayed. Rev. 2 placed +0.3 for "self before something greater" (Baralta "Faith is not mediated — it is lived", S9 `:100`) — the inward zealot; the inquisitor, the public debunker and the revivalist leader are all on a stage. The four split on display — 0 |
| D/I | **−0.3** | cited — **STANDS (outside the instruction; see the flag below)** | S1 §3.1 "principled rather than calculative; the believer accepts hardship for theological reasons"; §1b(c) faith↔deontological — Weber's conviction ethic. Checked against the four: the zealot and the revivalist are Weber's conviction type; the agnostic pursuing Truth accepts inconvenient findings (value-rational, not instrumental); the atheist discrediting religion is the one who may act instrumentally. Three of four hold, so the cell stays, small |

⚠ **The consequence Jordan should see, stated once.** Run to its end, the same logic zeroes Pa/Eq
and D/I too (each holds for three of four, not four of four), and an all-zero `faith` row is
**mechanically inert in `score`** (`choose.py:365-368`: `Σ axis_w·align` reads only the projected
axes) — a person's `faith` weight would then move nothing in DELIBERATE and matter only through
`Person.conviction`'s own machinery (H10/H11) and through the deontological gate's threshold on
whatever D/I the row keeps. The two cells are left standing so the row is not inert, and because the
instruction named four cells; whether they go too is Jordan's. §5.2 arm F measures the all-zero
case (−0.167) and arm G the D/I-only case (+0.123) so the choice is priced.

**How `faith` relates to `Person.conviction` — RULED (Jordan, 2026-09-27, same session), recorded
as a DESIGN NOTE, not built here.** Verbatim: *"faith as a pursuit is strongly modulated by
religious conviction."* This is the relationship between the two systems, not two independent
numbers that happen to coexist: the `faith` cell weight in `Person.pursuits` is the pursuit's
BASELINE magnitude — how much of a person's action and decision-making concerns religious matters
at all — and a person's PRACTICAL strength of acting on it is that weight SCALED by their
`Person.conviction` intensity. A high nominal `faith` weight with tepid conviction acts on it weakly;
the same nominal weight with intense conviction — the devout builder or the militant dismantler
alike — acts on it hard; and it is `Person.conviction` that supplies WHICH side and HOW intensely
(R1/R2, ED-IN-0251), which is the second reason (beside the four-example test above) that direction
and intensity do not belong in this row. ⚠ **Engineering boundary, stated as this file states every
other one:** this is H10/H11's territory once `Person.conviction` exists in code
(`PROPOSAL.md` §3.4 — it does not today; `church_standing` is one unread string, `rosters.yaml:387`).
The note for whoever builds it: the eventual score/decision formula should treat `faith`'s
projected contribution as interacting MULTIPLICATIVELY (or similarly) with the person's conviction
intensity — `w_faith · intensity · row_faith`, or an equivalent — **not** as two additive,
independent terms. Nothing in this file, in `choose.py:365-368`'s `Σ axis_w·align`, or in the worksheet
implements that; this grid resolves the CONTENT (the row's seven values) and records the relationship
so the mechanism is not re-derived. Unbuilt, out of scope.

*(The rev. 2 table this replaces is superseded in full; its H/E and D/I values are unchanged.)*

<!-- rev. 2 table follows for the record; its P/S, Se/Sl, R/F, G/Hu rows are SUPERSEDED by the table above -->
What survived in rev. 2 as "true of religious devotion on either side" — kept as the record of what changed:

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **0.0** | derived (DEPARTURE from `was:`) | S1 §3.1's +0.4 is explicitly the ecclesiastical ladder → `Person.conviction` (S4, S5 `:85`). Set to 0 so the side does not leak into the pursuit |
| P/S | **−0.3** | derived (halved from `was:`) | S1 §3.1 trad +0.6 "grounded in scripture and tradition … Not maximal because Faith can also be reformist"; S3 memory +0.4 / substantive −0.3. Halved because an Einhir *revivalist* also looks to a (different) past, so the lean is real but weaker than the Church's alone |
| Pa/Eq | **+0.2** | cited, reasoning re-grounded | S3 +0.2 kept. Substantive ground: religious devotion on either side carries a claim about how ALL people are to be treated under its law — the Church's "pastoral care extends to every territory" (S10 `:613`), the Einhir revival's claim for a suppressed people — which is the treatment-under-law strand; but each also has an inside and an outside (heretic, unbeliever), so only mild |
| Se/Sl | **+0.3** | derived | S3 selfish −0.1; S5 `:124-126` "how much of YOURSELF goes into religious matters" — self given over. Magnitude mine |
| R/F | **−0.4** | reasoned — **NOT re-examined in rev. 3, on Jordan's instruction**: this row is under separate consideration for the H7 regression (§5.2 arms E/F), and whatever is decided there moves the correlation as a side effect | no corpus citation on the axis; placed because devotion of either side holds its tenets AGAINST circumstance — Himlensendt "sincerely devout … his faith is the load-bearing wall" (S10 `:608`), the dismantler "PURE Einhir" (S5 `:128`) — and the pursuit of faith is the pursuit of that holding. Moderate rigid. ⚠ This cell and G/Hu are the two whose addition moves §5.2's arm A from pass to fail; see §5.2 arm E |
| G/Hu | **+0.3** | reasoned | no corpus citation; placed because giving oneself to something greater is the definition's shape (S5 `:124` "how much of yourself goes into religious matters") — Baralta's "Faith is not mediated — it is lived" (S9 `:100`) is the inward form. Mild humble; mild because the inquisitor and the public dismantler are both faith-pursuers with a stage |
| D/I | **−0.3** | cited | S1 §3.1 "principled rather than calculative; the believer accepts hardship for theological reasons" — true of the dismantler as of the builder |

**Phase 3 grounding — faith (rev. 5: RULED magnitude-only; the rev. 2 table above is superseded by the ruled table at the top of §2.11).** §1a faith already had the shape: Tillich's ultimate concern takes ANY object, and Jordan's four examples are four objects of one concern. H/E: 0.0 (ruled; Tillich). P/S: **CHANGED −0.3 → 0.0** — the four split on where the answer comes from. Pa/Eq: +0.2 STANDS — a one-rule-for-all shape common to the four, mild. Se/Sl: **CHANGED +0.3 → 0.0** — subject matter, not beneficiary. R/F: **CHANGED −0.4 → 0.0** — the disposition is the other pursuits'; §1b(a)'s Weber entailment (conviction persists) now reaches `score` through D/I only. G/Hu: **CHANGED +0.3 → 0.0** — display is the other pursuits'. D/I: −0.3 STANDS — three of four are Weber's conviction type.

### 2.12 `happiness` — was null

**No source anywhere in the tree** beyond the name in S4/S5; S4 lists it on NEITHER side of
self/other. **Working definition used for every cell below:** the pursuit of one's OWN contentment
— being well, feeling well — as distinct from the good of others (which is `love`/`community`) and
from being good (`virtue`). All seven are reasoned; none is cited.

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **0.0** | reasoned | placed at zero because contentment is found at every rung and the pursuit makes no claim about rank in either direction. A reasoned zero |
| P/S | **+0.3** | reasoned | placed because what contents ME is judged in the present case, not by what was done before — the pursuit looks to the situation. Moderate substantive |
| Pa/Eq | **−0.2** | reasoned | Substantive ground: the pursuit weighs one's own wellbeing first and is indifferent to distributive fairness or treatment under law as such — the smallest "own side", as `individuality`. Mild partisan |
| Se/Sl | **−0.4** | reasoned | placed on the self side although S4 did not list it there: by the working definition the pursuit is of ONE'S OWN state — a person pursuing another's happiness is pursuing `love` or `community`. Moderate, not strong, because S4's silence is the only fact and it cuts against a high magnitude |
| R/F | **+0.4** | reasoned — **re-examined rev. 3, KEPT** | placed because the pursuit takes whichever road leads to contentment and abandons one that does not — no form is held for its own sake. Under §0.5's test this is flexible in Jordan's exact sense: a course that has become difficult is, for this pursuit, a course that has stopped delivering, and is left. There is no registry instance either way (the row is definitional throughout); nothing to move it. Kept |
| G/Hu | **+0.1** | reasoned | placed slightly humble because contentment needs no audience — but display can itself be a pleasure, so near zero |
| D/I | **+0.4** | reasoned | placed because acts are weighed by whether they PRODUCE contentment, which is outcome-weighing — Jordan's `instrumental` (S5 `:64`). Moderate; a happiness that is spoiled by a disagreeable act is the counter-case and keeps it under 0.5 |

**Phase 3 grounding — happiness.** All seven CONFIRMED on §1a's HEDONIC reading (§1b(b) records that the row's independence from `virtue` rests on that reading). H/E: contentment at any rung: 0.0. P/S: what pleases is judged in the present case: +0.3. Pa/Eq: indifferent to fair treatment; the smallest own: −0.2. Se/Sl: subjective well-being is one's own; Schwartz hedonism: −0.4. R/F: §1a rigid/flexible — a road that stops delivering is left (exit): +0.4. G/Hu: contentment needs no audience: +0.1. D/I: Bentham's calculus is the instrumental paradigm: +0.4.

### 2.13 `family` — was null. Nearest OLD row: `Identity` [+0.4, +0.2, 0.0, +0.6] (S8 §2 "tribe, **lineage**, faction"); S3 `Identity` {+0.5, 0.0, −0.9, 0.0} — ANALOGY, weak

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **−0.3** | reasoned | no corpus citation for the pursuit; placed because a family in this setting is a RANKED structure — a hearth "with a head" (`proposals/2026-08-29-greenfield-systems-suite-v2/02_character_generation.md:394`), an heir designated by `succeed` ("the office outlives its holder unchanged", S2 `:1653`), a house name as a "deed-family mark" (Baralta, `04_seasons_duchies.md:59`) — so the pursuit of family is the pursuit of a place in a line. Identity's +0.4 ("lineage-based offices", S1 §3.10) is the analogy behind the magnitude, reduced |
| P/S | **−0.3** | analogy (weak) | S1 §3.10 "Identity is ancestral; lineage and tribal"; `succeed` "dynastic continuity" (S2 `:1653`). Magnitude mine |
| Pa/Eq | **−0.6** | analogy, reasoning re-grounded | S3 Identity −0.9 as the analogy. Substantive ground: kin are owed what strangers are not — the family is the narrowest "own side" there is, and distributive fairness across it and outsiders is precisely what a family-pursuer sets aside (Virke's "personal loyalty to partners vs family directives", S7 `:219`, is the conflict from the other end). Strong partisan; not maximal because `love` is narrower still |
| Se/Sl | **+0.5** | derived | S4: other side. Magnitude mine |
| R/F | **−0.3** | reasoned — **re-examined rev. 3, KEPT** | no corpus citation; placed because kin obligation is not renegotiated case by case — Virke: "Third conflict with family triggers enforcement" (S7 `:219`) — the form holds. Under §0.5's test: the family's directives are enforced, not adapted, when a member's course diverges — the family does not go looking for a different arrangement, it brings the member back. That is rigid on the family's side of the bond, and the line it holds is the inherited one (P/S −0.3). Kept; Laskaris's "PROTECTIVE — priority is Elske's safety … Flips if Elske Loyalty ≤ 2" (`:241`) is a conditional course change and keeps this moderate |
| G/Hu | **+0.3** | reasoned | no corpus citation; placed because the pursuit subordinates the self to the LINE — the heir, the house, the hearth outlast the person (as `succeed`'s reason). Moderate humble |
| D/I | **0.0** | analogy | S1 §3.10 instr 0.0 "Identity is intrinsic" |

**Phase 3 grounding — family.** H/E: §1a family — *familia* is a unit of domination under a head; Weber's patrimonial household: CONFIRMED −0.3. P/S: Bourdieu's strategies of reproduction — the line looks back to reproduce itself: CONFIRMED −0.3. Pa/Eq: §1b(c) family↔partisan — Williams, Nagel: CONFIRMED −0.6. Se/Sl: the line is a STAKE (Bourdieu), so less selfless than the stakeless fiduciary (warden): CONFIRMED +0.5. R/F: kin obligation is enforced, not renegotiated: CONFIRMED −0.3. G/Hu: the line over the person: CONFIRMED +0.3. D/I: Identity's "intrinsic" (S1): CONFIRMED 0.0.

### 2.14 `love` — was null

S12: `07_drift.md:153` "precisely what love asks for", `:308` "Exile does not protect the people who
love them" — love as the knot that carries the load; nothing about a moral axis.

**Working definition for the reasoned cells:** the pursuit of a particular other's good and of the
bond with them — the knot, in S12's vocabulary, that "carries the load" (`RULINGS.md:377-378`).

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **+0.3** | reasoned | no corpus citation on the axis; placed because love attaches to a PERSON regardless of station — S12 describes the knot as a bond between people, not between ranks (`06_operations.md:161` "threads are knotted to their relationships") — so it levels where it lands. Mild `equal`, mild because it levels one pair, not the ladder |
| P/S | **+0.4** | reasoned | no corpus citation; placed because love answers the person in front of you as they are now — S12 `07_drift.md:153`: bringing someone "back to who they were" is "precisely what love asks for", a judgment of THIS case. Moderate substantive |
| Pa/Eq | **−0.7** | reasoned | Substantive ground: love is for ONE — the beloved is not weighed against a fair distribution and is not treated under the same rule as everyone else; S12 `07_drift.md:308` "Exile does not protect the people who love them" — the knot is particular and does not generalise. The most partial pursuit on the grid; rev. 1 left this null for want of a line and Jordan's rev. 2 instruction asks for the reasoned placement instead |
| Se/Sl | **+0.7** | derived | S4: other side. Magnitude mine |
| R/F | **−0.4** | reasoned — **MOVED rev. 3** (was +0.3) | Rev. 2's "love bends for the beloved" described the MEANS yielding to the person, which §0.5's test does not measure; the test asks whether the COURSE is held when it gets hard. S12's own evidence answers rigid: `07_drift.md:308` "Exile does not protect the people who love them" — the bond holds despite distance and cost; `:290-291` "their threads are knotted to family, fellow practitioners, community; their frays wrap around everyone" — the knot carries the load rather than releasing it; `:153` love "asks for" the being back "to who they were" — an insistence, not an adaptation. Moderate-strong rigid. P/S stays +0.4 (love answers the person as they are now) |
| G/Hu | **+0.3** | reasoned | no corpus citation; placed because the self is given for another by definition. Moderate humble |
| D/I | **+0.1** | reasoned | no corpus citation; placed near zero, slightly instrumental: love does what the beloved's good NEEDS (the outcome for the other, `07_drift.md:153`) but also "will not" betray — the two pull against each other and the outcome side is only slightly stronger |

**Phase 3 grounding — love.** All seven CONFIRMED on §1a love (Frankfurt; care ethics; Tönnies's community of mind). H/E: love levels its pair: +0.3. P/S: answers the person as they are now (Giddens): +0.4. Pa/Eq: §1b(c) — caring-for THIS person; Williams: −0.7. Se/Sl: Frankfurt's disinterested concern: +0.7. R/F: §1b(c) love↔rigid — volitional necessity, the lover cannot will otherwise: −0.4 (rev. 3's move, now on the pursuit's content; this is §1b(a)'s rigid+substantive corner). G/Hu: self given for another: +0.3. D/I: the beloved's good needed vs "will not betray" — nearly cancel: +0.1.

### 2.15 `warden` — was `Warden` [+0.5, +0.4, −0.1, +0.4]; S3 `Warden` {−0.3, +0.6, −0.3, −0.5}

| axis | value | grade | citation |
|---|---|---|---|
| H/E | **−0.2** | reasoned — **CHANGED rev. 4** (was cited −0.5; §1a warden, RULED Southernmost-specific: the generic lord-steward rank reading does not fit an independent working order with a Warden-Chief and a Second Senior Warden, outside the caste ladder, keeping the substrate for everyone; what survives is seniority of the work) | corpus value beneath: S1 §3.11 "protective duty of the higher-rank to the lower (lord to peasant, steward to household)" — the generic reading, set aside; Edeyja `:25-45`, Orm `:795-813`; S5 `:54` "the only row touching the thread side" |
| P/S | **−0.1** | reasoned (conflict resolved) | S1 §3.11 trad +0.4 "continues ancestral patterns" → −0.4 against S3 memory −0.3 / substantive +0.6 and Edeyja "an empiricist by practice" (S9 `:221`). Resolved to a small negative: the Warden's work is a CONTINUING practice ("the work must continue", S7 `:43`; 31 years at the Southernmost, `:812`) executed by reading the substrate as it IS — the pursuit is of the practice (precedent) and the practice is substantive in method. The two nearly cancel |
| Pa/Eq | **−0.3** | cited, reasoning re-grounded | S3 −0.3 kept. Substantive ground: stewardship is owed to ONE'S OWN dependents — the household, the Southernmost practitioners Edeyja protects (S7 `:44`) — not to whoever stands before you; a warden who treated all alike would not be warding. Moderate partisan; moderate because the Southernmost work benefits the whole peninsula (Orm's Gap-sealing, `:812`) |
| Se/Sl | **+0.5** | cited | S3 selfish −0.5 — the strongest selfless cell on the old roster; Orm "The work. Only the work." (S7 `:811`), Edeyja/Orm `self_other_initial` −0.30/−0.20 |
| R/F | **−0.3** | reasoned — **re-examined rev. 3, KEPT** | no corpus citation on the axis; placed because the duty does not bend — "Continue the work regardless of interference" (S7 `:44`), "The work. Only the work." (`:811`). Under §0.5's test this is rigid verbatim — unwilling to deviate from the course in the face of difficulty (Orm's 31 years, the death-Mending, `:812`) — and it is rigid about a course that is NOT precedent-bound in method (P/S −0.1: Edeyja "an empiricist by practice", S9 `:221`). With P/S near zero this row barely enters the correlation either way. Kept |
| G/Hu | **+0.5** | reasoned | no corpus citation on the axis; placed because the Warden spends the self for the dependent — Orm's death-Mending sealing a Gap (S7 `:812`), "Chernobyl liquidator archetype", "Only the work" — the most self-effacing pursuit on the grid. Strong humble |
| D/I | **−0.1** | cited | S1 §3.11 "duty-bound; mildly anti-instrumental" |

**Phase 3 grounding — warden (Southernmost-specific per §1a; the generic theory is checked against it, not substituted).** H/E: §1b(c) warden↔hierarchical — the generic rank reading is ruled out by the Southernmost's own structure: **CHANGED −0.5 → −0.2**. P/S: the work is a continuing practice (31 years; "the work must continue") done by reading the substrate as it is (Edeyja "empiricist by practice"): CONFIRMED −0.1. Pa/Eq: §1b(c) — "protect Southernmost practitioners" is partial, the substrate-keeping is for all: CONFIRMED −0.3. Se/Sl: stakeless up to death-Mending (Orm): CONFIRMED +0.5. R/F: "Continue the work regardless of interference" — persistence in Jordan's sense: CONFIRMED −0.3. G/Hu: "Only the work" — self spent, no display: CONFIRMED +0.5. D/I: the work is done because it is the work, not for a calculated return: CONFIRMED −0.1.

### 2.16 The grid at a glance (rev. 4 — complete; ° = reasoned, no corpus citation; ⚠ = conflict resolved to one value; ▲ = moved in rev. 3 against §0.5's test; ▼ = changed in Phase 3 against §1b; ◆ = set by Jordan's `faith` ruling, rev. 5)

| pursuit | H/E | P/S | Pa/Eq | Se/Sl | R/F | G/Hu | D/I |
|---|---|---|---|---|---|---|---|
| virtue | −0.2 | −0.2 ⚠ | +0.3 | −0.2 | +0.2° | +0.2°▼ | −0.3°▼ |
| honour | −0.5 | −0.8 | −0.3 | +0.2°▼ | −0.6 | −0.4° | −0.7 |
| liberty | +0.7 | +0.5 | +0.2° | −0.1 | −0.3°▲ | 0.0° | +0.1 |
| justice | +0.4 | +0.1 ⚠ | +0.8° | +0.2 | −0.3° | 0.0° | −0.2 |
| wealth | −0.2° | +0.4 | −0.4° | −0.6 | +0.5° | 0.0°▼ | +0.6 |
| reputation | −0.3° | −0.2° | −0.3° | −0.6 | +0.3° | −0.4▼ | +0.3° |
| scholastics | −0.1 | −0.1 ⚠ | +0.4 | 0.0 | +0.3° | +0.2° | +0.3 |
| stability | 0.0 | −0.4 | +0.4 | 0.0 | −0.3▼ | +0.2° | +0.2 |
| individuality | +0.3° | +0.5° | −0.2° | −0.4▼ | −0.4°▲ | −0.1°▼ | 0.0° |
| community | 0.0 | −0.5 | −0.3° | +0.4▼ | −0.2° | +0.4° | −0.2 |
| faith | 0.0 | 0.0◆ | +0.2 | 0.0◆ | 0.0◆ | 0.0◆ | −0.3 |
| happiness | 0.0° | +0.3° | −0.2° | −0.4° | +0.4° | +0.1° | +0.4° |
| family | −0.3° | −0.3 | −0.6 | +0.5 | −0.3° | +0.3° | 0.0 |
| love | +0.3° | +0.4° | −0.7° | +0.7 | −0.4°▲ | +0.3° | +0.1° |
| warden | −0.2°▼ | −0.1 ⚠ | −0.3 | +0.5 | −0.3° | +0.5° | −0.1 |

**Tally (105, rev. 5):** cited **28** · derived/analogy **22** · reasoned **55** · **null 0**. Rev. 5
(Jordan's `faith` ruling, 2026-09-27) set faith P/S, Se/Sl, R/F, G/Hu to 0 as RULED cells (◆): two
were derived and two reasoned, all four are now cited. **Rev. 4's tally:** cited **24** ·
derived/analogy **24** · reasoned **57** · **null 0**. Phase 3
changed ten values (▼), all by magnitude and none by sign: virtue G/Hu +0.4→+0.2, virtue D/I
−0.5→−0.3, honour Se/Sl −0.1→+0.2, wealth G/Hu −0.2→0.0, reputation G/Hu −0.6→−0.4, stability R/F
−0.5→−0.3, individuality Se/Sl −0.7→−0.4, individuality G/Hu −0.4→−0.1, community Se/Sl +0.6→+0.4,
and warden H/E −0.5→−0.2 (on Jordan's ruling that `warden` is Southernmost-specific, §1a).
Three cited cells (virtue D/I, honour Se/Sl, warden H/E) became reasoned because the theory or the
ruling overrode the corpus number, with the corpus number kept beneath. **Rev. 2's tally for reference:** cited **27** ·
derived/analogy **24** · reasoned **54** · **null 0**. (Rev. 1 was
32 / 26 / — / 47; five cited and two analogy cells moved to *reasoned* because their value was
changed by a conflict resolution or by the equity correction.) The four ⚠ cells now carry one value
each; §7.2 records what each source said. **Rev. 3 changed three values (▲) and no grades**: the
three were already reasoned cells, so the tally is unchanged; the R/F column now reads 7 rigid / 5
flexible / 3 near-zero-P/S rows against rev. 2's 8 / 7, and both of §0.5's corners are occupied
(flexible+precedent: scholastics, reputation; rigid+substantive: liberty, individuality, love, justice).

---

## §3 · C1b — the alignment table, 42 verbs × 7 axes

Sparse, as today (`rosters.yaml:1535-1538`: `default_cell: 0.0` for an unlisted pair; the loader
refuses an all-zero table). Verb keys spelled as `verb_table.yaml` spells them. A cell marked
**carried** is an S2 cell moved per §0.4 with its original reason; **derived** is a direction read
off S13's row text or an S2 reason re-homed, magnitude mine.

### 3.1 `hierarchical↔equal` — S2's `hierarchical` block (`:1567-1591`) carried, sign per §0.1

| verb | value | grade | reason (S2's, unless noted) |
|---|---|---|---|
| determine | **−1.0** | carried | the licensed judgement made by the holder licensed to make it |
| confer | **−0.8** | carried | conferral seats an office; the paradigm top-down act |
| evade / defy | **+0.9** | carried | refusing a demand outright is the direct negation of command |
| establish | **−0.7** | carried | founding an office adds a rung to the ladder |
| revoke | **−0.7** | carried | an officeholder unmaking a subordinate's standing |
| issue | **−0.6** | carried | a dispensation is a remit reaching the executors named in scope |
| comply | **−0.6** | carried | obeying a dispensation's terms is literal deference to the issuer |
| levy | **−0.6** | carried | taking a rung's stores under a remit is rank drawing on subjects |
| dispatch | **−0.5** | carried | an order sent down the office to a named person |
| open_case | **−0.5** | carried | opening a case invokes the remit's institution over the matter |
| petition | **−0.4** | carried | the channel a subordinate has; using it works the hierarchy |
| repudiate | **+0.5** | carried | unmaking a commitment un-does a standing another's authority made |
| surveil | **+0.3** | carried | watching "without leave" is unauthorized by definition |
| destroy_record | **+0.4** | carried | defacing what an office's ruling produced |
| convene | **−0.4** | derived | S13 `:161-172`: a `remit:convene` act that "gathers a venue's rung" — the same remit-act family as `dispatch`/`issue`, which S2 celled and this one it omitted |
| carry | null | — | **deliberately absent**, as S2 `:1587-1591` records: "the lowest-magnitude, weakest-justified cell in the set"; kept absent |
| the other 26 | null | — | no S2 cell and no row text about rank |

### 3.2 `precedent↔substantive` — S2's `traditional` block (`:1643-1661`) carried, sign flipped (precedent = neg)

| verb | value | grade | reason |
|---|---|---|---|
| destroy_record | **+1.0** | carried | "unmaking the record is the anti-procedural act" — the record is what precedent is consulted in |
| create_record | **−0.8** | carried | "the record IS what precedent is made of" |
| research | **−0.7** | carried | "archives, oral histories, institutional records — continuity's own method" — fits Jordan's definition (S5 `:65`) exactly: looking to prior cases |
| succeed | **−0.6** | carried | "heir designation is dynastic continuity in one act" |
| tie / knot | **−0.5** | carried (⚠ weaker fit) | "the ancestral social technology" — that is *traditional*, not *where you look for the answer*; kept, flagged |
| repudiate | **+0.5** | carried | "breaks with the practice of keeping vows" |
| evade / defy | **+0.5** | carried | "breaks with the expected, established course" |
| reconstruct | **−0.4** | carried | "assembling what stands, not creating what is new" |
| confer | **−0.4** | carried | "office and title pass down established forms of investiture" |
| open_case | **−0.4** | carried | "a case still runs the stage-and-terms template §13.1 sets down — procedure by precedent" |
| oblige | **−0.3** | carried | "duty-taking has the same ancestral shape as any tie" |
| release | **+0.3** | carried | "the un-binding — runs opposite `tie / knot`" |
| construe | **+0.5** | derived | S2 `:1633` reason re-read on this axis: "a deliberate reading of the terms" — reading the instrument for THIS case rather than as it has been read; S13 `:459` "reading an instrument" |
| challenge | **−0.3** | derived (weak) | ED-IN-0261: "the duel pair" — a formal, established form; no stronger text |
| the other 28 | null | — | no source |

### 3.3 `partisan↔equitable` — no old block; every cell derived from S13/S2 row text

| verb | value | grade | reason |
|---|---|---|---|
| determine | **+0.6** | derived | S13 `:195-207`: the licensed judgement; its `beneficiary_note` says who it FAVOURS is the `judging_set` — the act's own form is impartial adjudication |
| construe | **−0.6** | derived | S2 `:1633` "calculated to serve the construer's aim, not to keep the bond" |
| forge | **−0.5** | derived | S2 `:1631` "counterfeiting a record for advantage" |
| open_case | **+0.3** | derived | S2 `:1659` "procedure by precedent" — the case runs by template regardless of who stands before it |
| levy | **−0.3** | derived | S2 `:1580` "rank drawing on subjects" — one's own office's take |
| the other 37 | null | — | no source. `transfer` (beneficiary `to`) and `tell` (beneficiary `subject`) are partial toward a person but toward WHOM is the candidate's fact, not the verb's |

### 3.4 `selfish↔selfless` — **no cells, by design (cited)**

S4: *"`benefits_me` and the 38-row beneficiary column SURVIVE — the selfish axis score supplies the
disposition, the column supplies the per-candidate fact."* The per-candidate fact is already
single-owned at `verb_table.yaml`'s `beneficiary:` column (actor / subject / to / none; e.g. `carry`
`:104-105`, `kill / wound` `:290-291`) and read by `benefits_me` in `decision/choose.py`. A
`selfish` row in `alignment` would be a second copy of that column (`CLAUDE.md` §0.05 cl.3).
**Recommendation for Jordan:** leave this axis out of `alignment` entirely; the axis reaches `score`
as `axis_w[selfish] × benefits_me(c)`, and the five new verbs need a `beneficiary:` cell each
(`kill`/`wound`/`fight`/`challenge`: `actor`, as the old `kill / wound` row; `accept`: `actor`).
**42 positions null with this reason.**

### 3.5 `rigid↔flexible` — no old block; derived

| verb | value | grade | reason |
|---|---|---|---|
| construe | **+0.7** | derived | bending the terms to fit (S2 `:1633`, S13 `:453-459`) |
| repudiate | **+0.5** | derived | un-binding a live commitment (S13 `:479-494`) |
| comply | **−0.4** | derived | S2 `:1579` "literal deference" to the terms |
| commit | **−0.4** | derived | S2 `:1629` "binds regardless of what later calculation would recommend" |
| release | **+0.3** | derived | S2 `:1661` "the un-binding" |
| oblige | **−0.3** | derived | S2 `:1603`/`:1660` "duty-taken … the vow's own form" |
| accept | **−0.3** | derived | accepting the challenge as offered — bound by its form (ED-IN-0261 "the duel pair") |
| tie / knot | **−0.2** | derived | S2 `:1600` "a bound tie" |
| the other 34 | null | — | no source |

### 3.6 `grandiose↔humble` — no old block; derived on `synthesis.md` §2's criterion ("acts that put him in front of witnesses")

| verb | value | grade | reason |
|---|---|---|---|
| challenge | **−0.6** | derived | the public challenge — putting oneself forward before witnesses; old `kill / wound` sacred reason "settled before witnesses" (S2 `:1612`) re-read here |
| speak | **−0.4** | derived | S13 `:531-541` emits `speech.made`, no subject, no writes — the one verb whose whole content is being heard. ⚠ Answers Jordan's Q1 on `speak`: **yes, one cell**, if this reading holds |
| fight | **−0.3** | derived | as `challenge`, without the declaration |
| establish | **−0.3** | derived | S2 `:1604` "founding a new office-seat" — adding a seat to the world |
| petition | **+0.3** | derived | S2 `:1583` "the channel a subordinate has" |
| accept | **−0.2** | derived | as `fight` |
| tell | null | — | S13 `:560-608`: one-to-one deposit with the subject; not a witnessed display. ⚠ Answers Jordan's Q1 on `tell`: **no cell on any axis from this draft** — testimony's moral weight is in WHAT is told (a claim), which no verb×axis cell can carry. Flagged §7 |
| the other 35 | null | — | no source |

### 3.7 `deontological↔instrumental` — S2's `instrumental` block (`:1619-1641`) carried unchanged (S6 lineage), plus re-homed `sacred` reasons and the five new verbs

| verb | value | grade | reason |
|---|---|---|---|
| forge | **+0.8** | carried | "the purest means-to-ends act on the table" |
| commit | **−0.8** | carried | "binds regardless of what later calculation would recommend — Honour's own −0.7 shape" |
| utter | **−0.7** | carried | "the uttered word binds the utterer whatever advantage later counsels" |
| evade / defy | **+0.7** | carried | "putting your own calculus over a demand" |
| construe | **+0.7** | carried | "calculated to serve the construer's aim" |
| exchange | **+0.6** | carried | "ledger-logic, no oath behind either side" |
| transfer | **+0.6** | carried | "bald calculation, stripped of any binding or vow" |
| comply | **+0.5** | carried | "the safe route is obeying — the lower-risk, calculated path" |
| move | **+0.5** | carried | "leaving is the cheapest safety there is" |
| reconstruct | **+0.4** | carried | "the free, riskless route" |
| work | **+0.4** | carried | "presence converted into yield" |
| research | **+0.3** | carried | "the lower-cost, calculated route to a finding" |
| surveil | **null** | **CONFLICT** | S2 carried **−0.8**, but its own reason is *"priced by canon, not judged — fieldwork_v30 §4.2 charges Surveil +2 Exposure"* — a COST wearing an axis cell. On the new axis −0.8 would say surveillance is a *principled* act, which nobody argues. Recommend null; old value shown so nothing is lost silently |
| interview | **null** | **CONFLICT** | S2 carried **−0.3**, reason "the hand-revealing cost `research` avoids" — a price, same defect. Recommend null |
| repudiate | **+0.5** | derived (re-homed from `sacred −0.6`) | S2 `:1617` "breaking a live commit breaks the vow itself" — on this axis, the outcome over the bond |
| oblige | **−0.3** | derived (re-homed from `sacred +0.4`) | S2 `:1603` "duty-taken has the same vow-shape as `commit`" |
| tie / knot | **−0.4** | derived (re-homed from `sacred +0.7`) | S2 `:1600` "the consecrated bond" — binding oneself, as `commit` |
| kill | **+0.7** | derived | ED-IN-0261: "a deontologist as a score term is an instrumentalist with a strong preference" — this is the act the gate exists for; `verb_table.yaml:298`: "everything about whether the person WANTS to is `score` and the deontological gate". Magnitude mine |
| wound | **+0.4** | derived | as `kill`, lesser |
| fight | **+0.3** | derived | ED-IN-0261: "the attempt" |
| challenge | **−0.3** | derived | honour's act — issued regardless of outcome (§2.2 honour D/I −0.7) |
| accept | **−0.4** | derived | accepting regardless of odds — the same shape, stronger, because the acceptor did not choose the ground |
| thread_read | null | — | S2's rule kept (`:1564-1566`): no typed cell (`H-85`), not in `resolvable_verbs()`, no Candidate ever forms |
| the other 19 | null | — | no source |

### 3.8 Tally (294)

| axis | filled | carried | derived | null |
|---|---|---|---|---|
| hierarchical↔equal | 15 | 14 | 1 | 27 |
| precedent↔substantive | 14 | 12 | 2 | 28 |
| partisan↔equitable | 5 | 0 | 5 | 37 |
| selfish↔selfless | 0 | 0 | 0 | 42 (by design, §3.4) |
| rigid↔flexible | 8 | 0 | 8 | 34 |
| grandiose↔humble | 6 | 0 | 6 | 36 |
| deontological↔instrumental | 20 | 12 | 8 | 22 (2 are CONFLICT-null) |
| **total** | **68** | **38** | **30** | **226** |

Old density was 52 of 152 (~34%); this is 68 of 294 (~23%), and 68 of 252 (~27%) once the
by-design column is excluded. The worksheet (`:158-159`) says not to scale the old density, and this
does not: every carried cell is one S2 cell moved once.

---

## §4 · C2 — migration of characters and role templates to the fifteen

### 4.1 The derivation rule (so Jordan can accept a RULE rather than 44 hand edits)

| old name | new name | grade | source |
|---|---|---|---|
| Faith, Virtue, Honor, Liberty, Scholastic, Community, Warden | faith, virtue, honour, liberty, scholastics, community, warden | lineage | S5 `:41-54`, `:107-121` `was:` |
| Order | stability | ruled rename chain | S5 `:47` "was `order`, then `authority`"; S4 |
| Authority | stability | same | S5 `:47`; S4 refuses `authority` as a pursuit (property of the seat). ⚠ For clergy the old `Authority` is the ecclesiastical ladder — arguably `Person.conviction` intensity rather than any pursuit; noted per row |
| Equity | justice | **analogy — Jordan to confirm** | §2.4's argument; `PROPOSAL.md:660` calls Equity an orphan |
| Utility | **no successor** — an axis pole now (`instrumental`) | redistribute per character to the pursuit the character's own `goals:` / `arc_trajectory:` / `conviction_notes:` name; if none, DROP the weight and say so | S6, S4. **Every such row is flagged** |
| Precedent | **no successor** — an axis pole now (`precedent`) | as Utility: usually `stability` (the procedural readers) or `justice` (Baralta) | S4 |
| Identity | **no successor** | as Utility: usually `community` (the categorical belonging), which collapses S8 §2.1's Community/Identity split — flagged | S8 §2.1 |

Weights are carried at their old magnitudes; nothing is renormalised (the registry's own blocks do
not sum to 1 — Torsvald `0.40 + 0.20`).

### 4.2 The six role templates (`rosters.yaml:1381-1417`, from S10 §4)

| template | old (S10) | proposed new | flags |
|---|---|---|---|
| sovereign | Virtue .30, Authority .30, Honor .20, Faith .10, Warden .10 | virtue .30, **stability .30**, honour .20, faith .10, warden .10 | clean under 4.1 |
| ecclesiastical | Faith .40, Authority .20, Scholastic .20, Precedent .10, Virtue .10 | faith .40, **stability .20**, scholastics .20, **[Precedent .10 → stability, giving stability .30]**, virtue .10 | ⚠ Precedent orphan; alternative: fold the .10 into faith (.50) |
| mercantile-procedural | Order .35, Utility .25, Scholastic .20, Liberty .10, Equity .10 | **stability .35**, **[Utility .25 → wealth .25]**, scholastics .20, liberty .10, **justice .10** | ⚠ Utility orphan → `wealth` on the template's name ("mercantile") and its faction's goals (Feldhaus S7 `:188`); Equity → justice analogy |
| intelligence-diplomatic | Scholastic .30, Utility .30, Authority .20, Precedent .10, Identity .10 | scholastics .30, **[Utility .30 → ?]**, **stability .20**, **[Precedent .10 → stability → .30]**, **[Identity .10 → ?]** | ⚠⚠ **HALF THE VECTOR IS ORPHANED and the template is held by no faction** (`rosters.yaml:1375-1376`). No goals text to read from. Recommend Jordan either drops the template or names the two |
| reformist | Equity .30, Liberty .25, Community .20, Virtue .15, Scholastic .10 | **justice .30**, liberty .25, community .20, virtue .15, scholastics .10 | clean given Equity → justice |
| military-order | Honor .30, Authority .25, Virtue .15, Identity .15, Order .15 | honour .30, **stability .25 + .15 = .40**, virtue .15, **[Identity .15 → community .15]** | ⚠ two old names collapse into `stability .40`, which changes the template's shape (was Honor-led, becomes stability-led); Identity → community on S8 §2.1's "faction" reading. Varfell and Löwenritter share this vector (S10 `:197`) |

### 4.3 Per-character (`references/npc_registry.yaml`, line of the `convictions:` key)

Weights are the registry's own. ⚠ marks a row Jordan must confirm; **clean** means only 4.1's
lineage/rename rows were needed.

| id · name (line) | old | proposed new | flag |
|---|---|---|---|
| NPC-001 Edeyja (`:37`) | Warden .40, Precedent .20 | warden .40, **community .20** | ⚠ Precedent orphan; goals "Protect Southernmost practitioners" (`:44`) → community. Alt: warden .60 (Holdar/Orm shape) |
| NPC-002 Maret Uln (`:62`) | Equity .50, Warden .30 | justice .50, warden .30 | clean (Equity→justice) |
| NPC-003 Yrsa Vossen (`:86`) | Equity .40, Warden .25 | justice .40, warden .25 | ⚠ S9 `:161` "The community is the only legitimate political unit" — alt: community .40 |
| NPC-004 Sæmund Haelgrund (`:110`) | Faith .60, Authority .20 | faith .60, stability .20 | ⚠ Church `Authority` = the ecclesiastical ladder; alt: faith .60 alone + `Person.conviction` intensity |
| NPC-005 Sigrid Torsvald (`:134`) | Utility .40, Honor .20 | **warden .40**, honour .20 | ⚠ Utility orphan; goals "Minimize Thread collateral", arc "risk-averse on Thread collateral … perceives damage" (`:141-142`) → warden. Alt: stability .40 ("Mission success") |
| NPC-006 Halvar Brandt (`:157`) | Honor .35, Authority .25 | honour .35, stability .25 | clean |
| NPC-007 Annika Feldhaus (`:181`) | Utility .50, Community .10 | **wealth .50**, community .10 | ⚠ Utility orphan; goals "Maximize Guilds Wealth", "PROFIT-MAXIMISING" (`:187-189`) |
| NPC-008 Peder Almstedt (`:204`) | Order .40, Precedent .20 | stability **.60** | ⚠ Precedent orphan; "Maintain procedural correctness" (`:211`) → stability |
| NPC-009 Gerik Strand (`:227`) | Authority .30, Utility .30 | stability .30, **reputation .30** | ⚠ Utility orphan; "Maintain personal indispensability", OVERPERFORMER, flattery vulnerability (`:233-235`) → reputation |
| NPC-010 Dalla Virke (`:250`) | Utility .30, Honor .30 | **wealth .30**, honour .30 | ⚠ Utility orphan; "Maintain Virke trade network" (`:257`) |
| NPC-011 Alexios Laskaris (`:274`) | Virtue .50, Authority .20 | virtue .50, stability .20 | clean; note goals "Protect Elske's safety" (`:281`) — a `family` weight Jordan may want to add |
| NPC-012 Rikard Solberg (`:297`) | Utility .30, Order .30 | **wealth .30**, stability .30 | ⚠ Utility orphan; "Maintain stable trade" (`:304`). Alt: stability .60 |
| NPC-013 Aldric Tormann (`:320`) | Order .50, Liberty .30 | stability .50, liberty .30 | ⚠ the block's own `migration_notes` (`:326`) says "Faith + Order + Utility" and its goals say "Maximize Church Wealth throughput" — the OLD block already disagrees with itself; alt: stability .50, wealth .30 |
| Almud Almqvist (`:348`) | Virtue .45, Authority .30 | virtue .45, stability .30 | clean |
| Arne Himlensendt (`:373`) | Faith .50, Authority .20 | faith .50, stability .20 | ⚠ as Haelgrund |
| Elske Almqvist (`:403`) | null | null | — |
| NPC-031 Torben (`:423`) | null (ED-618 emergence window) | null | — |
| NPC-032 Lenneth Almqvist (`:442`) | Equity .45, Liberty .25 | justice .45, liberty .25 | clean |
| NPC-033 Kolbrun Thale (`:466`) | Liberty .30, Utility .30 | liberty .30, **[Utility .30 DROPPED]** | ⚠ Utility orphan and no `goals:` (`:473`); nothing to read from. Alt: scholastics .30 (spymaster) |
| NPC-034 Gustav Linder (`:490`) | Faith .60, Authority .20 | faith .60, stability .20 | ⚠ as Haelgrund |
| NPC-035 Theodor Kreutz (`:513`) | Order .35, Authority .25 | stability **.60** | ⚠ two names collapse to one |
| NPC-036 Wilhelm Voss (`:536`) | Order .35, Authority .25 | stability **.60** | ⚠ as Kreutz |
| NPC-037 Annalie Reichard (`:559`) | Precedent .35, Authority .25 | stability **.60** | ⚠ Precedent orphan; Lord Treasurer, Resonant Style Evidence (`:565`). Alt: stability .25, scholastics .35 |
| NPC-038 Arnlod Olafsson (`:589`) | Faith .60, Authority .20 | faith .60, stability .20 | ⚠ as Haelgrund; "Cardinal Justice" → alt justice .20 |
| NPC-039 Magnus Klapp (`:613`) | Scholastic .35, Faith .25 | scholastics .35, faith .25 | clean |
| NPC-040 Osten Jarnstal (`:637`) | Faith .50, Order .30 | faith .50, stability .30 | note `:643` names Honor (Templar) — alt honour .30 |
| NPC-041 Aldric Hann (`:664`) | null | null | — |
| NPC-050 Inge Baralta (`:684`) | Precedent .50, Authority .30 | **justice .30, stability .50** | ⚠ Precedent orphan; S9 `:99` "Constitutional procedure IS justice"; goals "Sovereign Authority Doctrine … parliamentary sovereignty" (`:691`). Split is mine |
| Magnus Vaynard (`:708`) | Equity .35, Utility .30 | justice .35, **individuality .30** | ⚠ Utility orphan; "ego-driven, wants to be the one who tears down the order" (`:628`). ⚠ **Registry-internal conflict:** it writes `self_other_initial −0.40` as "ego-driven", but S8 §3 makes NEGATIVE = selfless. Not this file's to fix; recorded |
| NPC-070 Lisbeth Ehrenwall (`:732`) | Order .60, Liberty .20 | stability .60, liberty .20 | clean |
| NPC-071 Torvi Heljason (`:748`) | Precedent .70 | **stability .40, scholastics .30** | ⚠ Precedent orphan; Legal Advisor, Evidence style. Split is mine |
| NPC-072 Olaf Geirson (`:762`) | Order .70 | stability .70 | clean |
| NPC-073 Björn Holdar (`:776`) | Warden .70 | warden .70 | clean |
| NPC-074 Ingrid Stenskald (`:790`) | Community .70 | community .70 | clean |
| NPC-075 Orm (`:807`) | Warden .60, Equity .20 | warden .60, justice .20 | clean |
| NPC-080 Vidar Haldorsen (`:825`) | Honor .60, Utility .20 | honour .60, **[Utility .20 → stability .20]** | ⚠ Utility orphan; "doctrine-following … Completes missions" (`:819`, `:829`) |
| NPC-081 Uta Falkenrath (`:840`) | Community .50, Precedent .30 | community .50, **stability .30** | ⚠ Precedent orphan; "commune voice against city power-politics" — alt community .80 |
| NPC-082 Njal Torberg (`:855`) | Identity .60, Honor .20 | **community .60**, honour .20 | ⚠ Identity orphan; "Fights for Einhir, not Vaynard" (`:859`) — categorical belonging read as community |
| NPC-083 Hedda Kronvald (`:871`) | Authority .50, Order .30 | stability **.80** | ⚠ two names collapse |
| NPC-084 Frieda Kessler (`:886`) | Community .70 | community .70 | clean |
| NPC-085 Nessa Grindvold (`:900`) | Liberty .50, Scholastic .30 | liberty .50, scholastics .30 | clean |
| NPC-086 Joren Bergvall (`:915`) | Scholastic .60, Utility .20 | scholastics .60, **[Utility .20 DROPPED]** | ⚠ Utility orphan; "Has data proving…" — alt scholastics .80 |
| NPC-087 Uwe Askeland (`:930`) | Community .50, Equity .30 | community .50, justice .30 | clean |
| NPC-088 Carin Vedel (`:945`) | Liberty .60, Equity .20 | liberty .60, justice .20 | clean |
| NPC-089 Zoe Palaiologina (`:960`) | Identity .50, Authority .30 | **[Identity .50 → ?]**, stability .30 | ⚠⚠ Identity orphan with nothing to read from ("Sincere imperialist"); community .50 is the 4.1 default and reads wrong for an imperial governor. **Jordan's call** |
| NPC-090 Stephanos Doukas (`:975`) | Precedent .50, Order .30 | stability **.80** | ⚠ Precedent orphan; "Enforces ancient trade treaties" — alt stability .50, wealth .30 |

**Counts:** 44 blocks with weights, 3 null. **Clean: 18.** Flagged: 26, of which Utility-orphan 10,
Precedent-orphan 9, Identity-orphan 2, clergy-Authority 5 (overlapping). Two rows (Thale, Bergvall)
drop a weight rather than invent a home; one (Palaiologina) is left to Jordan.

### 4.4 The migration surface every consumer must see

`PROPOSAL.md` §2.2: the `npc_registry.yaml` half RAISES on an old name (`pursuits.py:39-56`), the
`role_template_pursuits` half is SILENT (`pursuits.py:79-86` skips an unknown row). The
`stability`-collapses in 4.2/4.3 are the cells where a silent miss would be least visible, because a
template that lost `Authority` still has `Order`'s share and produces a plausible-looking number.

---

## §5 · C2's H7 pair, placed, and the self-check (measured)

### 5.1 The two placements (Jordan's words, S5 `:127-129`; weights are mine, modelled on S7 rows)

| | pursuits | modelled on |
|---|---|---|
| **builder** — "a devout church of Solmund follower [who wants] to do work for the church" | faith .45, stability .20, honour .15, community .10, virtue .10 | the clergy blocks (Faith .50-.60 + Authority .20 → faith + stability), with honour/virtue from the ecclesiastical template's Virtue .10 |
| **dismantler** — "pure Einhir and anti Solmund church whose faith work is about dismantling it" | faith .45, liberty .20, justice .15, community .10, individuality .10 | Lenneth (Equity .45, Liberty .25, "Einhir revival … Caste dismantlement"), Vedel (Liberty .60, Equity .20), with community for the Einhir belonging |

### 5.2 The check — run, not hand-computed

Instrument: `/tmp/…/scratchpad/h7_check.py` (this session; reproduced below so it is re-runnable),
projecting each placement through §2.16 (rev. 2, no nulls), then `cos = v_b·v_d / (|v_b||v_d|)`;
bar is ED-IN-0214's **cos ≤ 0.5** (60°). Six arms — the original four re-run on the completed grid,
plus two diagnostics on the `faith` row. Rev. 1's numbers are kept in the last column so the effect
of filling 47 cells is visible.

| arm | builder (rev. 5) | dismantler (rev. 5) | **cos rev. 5** | verdict | rev. 4 | rev. 3 | rev. 2 | rev. 1 |
|---|---|---|---|---|---|---|---|---|
| **A** — the draft weights above, the §2 cells | [−0.095, −0.270, +0.125, +0.050, −0.150, +0.040, −0.250] | [+0.230, +0.115, +0.200, +0.010, −0.165, +0.030, −0.165] | **+0.229** | **SEPARATES** | +0.635 | +0.648 | +0.540 | +0.437 |
| **B** — same, `faith .60` each (the registry's clergy shape), others .40 | [−0.050, −0.210, +0.140, +0.060, −0.140, +0.040, −0.230] | [+0.180, +0.060, +0.210, +0.040, −0.110, +0.040, −0.200] | **+0.524** | FAILS, by 0.024 | +0.850 | +0.854 | +0.810 | +0.675 |
| **C** — `faith .70` + one other pursuit (.30) each | [0, −0.120, +0.260, 0, −0.090, +0.060, −0.150] | [+0.210, +0.150, +0.200, −0.030, −0.090, 0, −0.180] | **+0.527** | FAILS, by 0.027 | +0.850 | +0.862 | +0.786 | +0.689 |
| **D** — arm A's weights, `faith` row's H/E, P/S carried AS `was:` (−0.4, −0.6) | — | — | **+0.761** | FAILS (control: the old row) | +0.761 | +0.779 | +0.761 | +0.708 |
| **F** (diagnostic) — arm A, with the `faith` row ALL zero | — | — | **−0.167** | separates | −0.167 | −0.111 | −0.499 | — |
| **G** (diagnostic, new) — arm A, `faith` row D/I −0.3 only (Pa/Eq also zeroed) | — | — | **+0.123** | separates | — | — | — | — |

*(Arm E — "the two disposition cells zeroed" — is no longer a diagnostic: the enacted row IS arm E
plus P/S and Se/Sl zeroed, so it is arm A.)*

**Read plainly: the enacted row makes Jordan's pair separate at the draft weights (arm A +0.229,
comfortably inside the 60° bar) and the control arm D shows it was the old `faith` row that had been
failing it (+0.761 unchanged).** Arms B and C, where `faith` is .60–.70 of the person, now fail by
0.024 and 0.027 — a hair, and for a reason the `faith` row can no longer fix: with the shared row
carrying only Pa/Eq +0.2 and D/I −0.3, what is left in common between the two people is the OTHER
pursuits' agreement on R/F (both rigid: stability/honour vs liberty/justice) and on D/I (both
conviction-type), which §1b(c) grounds as genuine content of those pursuits. At .60/.70 the four
other pursuits are 0.30–0.40 of the vector and those two shared columns tip the cosine just over
0.5. Arm G prices the next step (D/I only: +0.123) and arm F the last (all zero: −0.167) — either
would pass B and C too, at the cost §2.11 flags (a row that projects nothing is inert in `score`).
**The fix went to C1, not to code, as `PROPOSAL.md:503-504` requires; whether "HIGH on faith"
means .45 (passes) or .60 (fails by 0.02) is the one thing this table cannot decide.**

### 5.3 The aggregate check — `conviction_spread` on the whole draft grid (measured)

```
python -m engine.season.harness.conviction_spread --candidate <the 15x7 JSON written by h7_check.py>
```

| quantity | old 13×4 (ED-IN-0214) | rev. 1 (47 nulls) | rev. 2 (complete) | rev. 3 (R/F re-check) | **rev. 4 (Phase 3)** |
|---|---|---|---|---|---|
| `within_60deg` | 9 of 13 | 4 of 15 | 3 of 15 | 5 of 15 | **5 of 15** (warden +0.827, family +0.778, community +0.764, faith +0.631, love +0.583) |
| mean-vector magnitude | — | 0.168 | 0.113 | 0.175 | **0.184** |
| effective axes (PR) | 1.849 of 4 (`PROPOSAL.md:266`) | 3.31 of 7 | 3.54 of 7 | 3.95 of 7 | **3.69 of 7** |
| precedent↔substantive × rigid↔flexible | — | +0.574 | **+0.776** | +0.284 | **+0.257** |
| selfish↔selfless × grandiose↔humble | — | +0.397 | **+0.755** | +0.755 | **+0.608** |
| rigid↔flexible × deontological↔instrumental | — | +0.306 | +0.636 | +0.589 | **+0.703** (now the top pair) |
| selfish↔selfless × rigid↔flexible | — | +0.080 | −0.516 | −0.507 | **−0.680** |
| hier↔equal × prec↔subst | +0.743 (hier × trad) | +0.735 | +0.645 | +0.645 | **+0.681** (rose with warden H/E −0.5 → −0.2: warden had been the one hierarchical row with near-zero P/S, an off-pattern point the Southernmost ruling removed) |
| prec↔subst × deont↔instr | — | +0.678 | +0.580 | +0.580 | **+0.594** |
| selfish↔selfless × deont↔instr | — | −0.244 | −0.348 | −0.348 | **−0.518** |

**Rev. 5 (the `faith` row enacted, four cells → 0), same instrument:**

| quantity | rev. 4 | **rev. 5** |
|---|---|---|
| `within_60deg` | 5 of 15 | **4 of 15** (warden +0.793, family +0.761, community +0.704, love +0.600; faith now −0.326, a dissent) |
| mean-vector magnitude | 0.184 | **0.148** |
| effective axes (PR) | 3.69 of 7 | **3.81 of 7** |
| hier↔equal × prec↔subst | +0.681 | **+0.693** (top pair now; S1 lineage) |
| selfish↔selfless × rigid↔flexible | −0.680 | **−0.667** |
| rigid↔flexible × deont↔instr | +0.703 | **+0.640** (faith's R/F −0.4 / D/I −0.3 was one of its points) |
| selfish↔selfless × grandiose↔humble | +0.608 | **+0.592** |
| prec↔subst × deont↔instr | +0.594 | **+0.551** |
| prec↔subst × rigid↔flexible | +0.257 | **+0.228** |

Every correlation fell except the S1-lineage pair, and `faith` moved from the fourth-closest row to
the mean (+0.624) to a dissent (−0.326) — which is what a magnitude-only row should do: it no
longer votes with the belonging cluster. The paragraph below was written for rev. 4 and its
reasoning is unchanged by rev. 5; the figures it quotes are rev. 4's.

**Did the theoretical grounding reduce the correlation defects, or explain why they stand? Both,
and the file can say which is which.** The one correlation §1b(a) found to be a genuine
double-count — P/S × R/F, where S1's `traditional` column had been read as both "looks to the past"
and "holds its course" — fell from +0.776 to +0.257 once R/F was placed on persistence evidence
alone; its residual is honour and stability, where Weber's traditional authority and Hirschman's
loyalty genuinely co-occur, and both corners Jordan named are now occupied (flexible+precedent:
scholastics, reputation; rigid+substantive: liberty, individuality, love, justice). Se/Sl × G/Hu
fell from +0.755 to +0.608 by populating the cross corners the literature populates (honour
selfless+grandiose via Bourdieu; wealth at zero via Weber-against-Veblen; individuality near-humble
via Mill/Tocqueville), and it STANDS at that level because Schwartz's circumplex puts selfishness and
display in one region (self-enhancement) — the residual is the theory's prediction, not a
double-count, and the fifteen contain no strongly selfish+humble pursuit to pull it lower. Two
correlations ROSE, and §1b(a) says why each is expected rather than defective: R/F × D/I (+0.703,
now the top pair) is Weber's own entailment — the conviction-ethicist is defined by persisting when
results are bad — and could only be lowered by placing a deontological pursuit flexible, which the
theory forbids; Se/Sl × R/F (−0.680) is Tönnies — every "other-side" pursuit in the fifteen is a
Gemeinschaft bond (love, family, community, warden, faith), and a Gemeinschaft bond is by definition
one not exited under difficulty (Frankfurt's volitional necessity; care ethics), while the self-side
pursuits are Hirschman's exit (wealth, happiness, reputation). That last pair is the one to watch:
it is theory-consistent, but it means "for whom" and "holds course" cannot be varied independently
across THESE fifteen, and a rigid self-side pursuit other than `individuality` (D/I 0.0, so it does
not help R/F × D/I either) does not exist on the roster. H/E × P/S (+0.681) is the S1 lineage and
rose slightly when the Southernmost ruling moved warden's H/E toward zero — warden had been the one
hierarchical row with a near-zero P/S, so the ruling removed an off-pattern point rather than adding
a defect; PR settled at 3.69 of 7, up from rev. 2's 3.54 and down from rev. 3's 3.95 because Phase
3's magnitude reductions on Se/Sl, G/Hu and (for warden) H/E shrank three columns' variance. Where the file leaves a
correlation standing, the cell driving it now cites the theory that predicts it; where it reduced
one, §1b(a) is the reason, not a number chosen after the fact.

### 5.4 The instrument (so §5.2 is re-runnable without this session)

```python
# rows = §2.16 (rev. 2 has no nulls; rev. 1 used null -> 0.0), axes in pursuit_axes order; sign per §0.1
def project(rows, w): return [sum(w[p]*rows[p][i] for p in w) for i in range(7)]
def cos(a, b):
    import math; d = sum(x*y for x, y in zip(a, b))
    return d / (math.sqrt(sum(x*x for x in a)) * math.sqrt(sum(y*y for y in b)))
```
with arm A's weights `{"faith": .45, "stability": .20, "honour": .15, "community": .10, "virtue": .10}`
and `{"faith": .45, "liberty": .20, "justice": .15, "community": .10, "individuality": .10}`.

---

## §6 · G-Q5 — RECOMMENDATION FOR JORDAN TO ACCEPT OR REJECT (not a ruling)

**Question (`PROPOSAL.md:663`):** sum, precedence, or neither; and if precedence, a name.

**Recommendation: NEITHER as a new per-person object — keep gate-then-score, drop `PROPOSAL.md` §7
steps 3-6 (H12), and re-ask only against a measurement.** Concretely: no `Person.precedence` field,
no ordered tuple of tests; the deontological refusal at `opening_set` (ED-IN-0261) is the one
lexical EXCLUDE, and `Σ axis_w·align + stance_toward + u` (`choose.py:365-368`) stays the ranking.

Reasons, each with its source:

1. **The thing a precedence uniquely buys is already ruled and is a gate, not a slot.** A sum cannot
   express refusal ("at tau=0.1 a good enough outcome outranks any finite penalty", S4). ED-IN-0261
   gave that to `opening_set` as "one mechanism, not two" (S5 `:222-226`). `PROPOSAL.md` §2.1 step 1
   already concedes the Principle test is therefore gate-then-score. What remains for a precedence is
   Obligation, Threat, Standing, Habit, Conviction — and:
2. **Measured, that remainder is a no-op today.** `PROPOSAL.md` §6: candidates 28/28/28, one subject
   for all 46, "three of the six tests fire zero times", "the precedence band is, with respect to the
   person, currently a no-op" (`03_DECISIONS.md:68` confirms the probe re-run). Building it now
   violates `CLAUDE.md` §0.2 — nothing could execute it — and `PROPOSAL.md` §8's own falsifier ("the
   precedence is decoration if … the six tests produce the same act order as the score") cannot be
   run until the aperture work lands.
3. **The argument FOR precedence lost its central support.** `PROPOSAL.md` §4 F1: the sum's minus
   sign (`synthesis.md` §1.3 `cost` on the Ob) is free — the obstacle is already RESOLVE-side. F5
   deletes the global sum "on F1–F3 rather than on age", but F1 cuts both ways: with `cost` gone there
   is no term the sum mis-handles that the gate does not now catch.
4. **`Person.precedence` is another producer-less interior row.** `PROPOSAL.md` §5 item 2 says so
   itself ("fails the same disqualifier `convictions` fails"; the H-62 family). ED-IN-0261's R7
   dissolution removed the reason to hold per-person state beside the pursuit vector.
5. **The dilemma (`PROPOSAL.md` §3.6) survives without a precedence.** A deontological refusal that
   empties `live` IS the excluded-to-empty case; the `choose.py:347-350` split and an emitting null
   act ride the gate. §7 steps 1, 2 and 7 keep their value; 3-6 do not.

**If Jordan nonetheless wants an ordered tuple, the name:** `precedence` — measured free and already
used in exactly this sense in the tree (`PROPOSAL.md` §2.4: `harness/populated.py:148` "a precedence
list"; `hole_register.yaml:1664`), passing §4's cold-reader test. Second choice `priorities` (ordinary
word, same meaning, no collision found by a grep of `engine/season` for `priorit`). Not `docket`
(`w.docket` is the world's register), not `order` (442 hits, S4).

**What would show this recommendation wrong:** the aperture work lands, the probe's arm 3 shows the
aperture is no longer constant per person, and PROPOSAL §8's runnable comparison shows the six tests
would order acts differently from the score in a way the design wants. Then H12 is worth its field.

---

## §7 · Gap list and conflict list

### 7.1 Projection: the 55 REASONED cells (rev. 1's 47 nulls + 7 re-graded in rev. 2 + 3 in Phase 3: virtue D/I, honour Se/Sl, warden H/E − 2 re-graded to cited by the rev. 5 `faith` ruling: faith R/F, G/Hu), by axis

Zero nulls remain in §2. Every cell below carries its reasoning in its own row; this is the index.

| axis | reasoned rows | of which rev. 1 null |
|---|---|---|
| H/E | wealth, reputation, individuality, happiness, family, love | 6 |
| P/S | virtue⚠, justice⚠, scholastics⚠, warden⚠, reputation, individuality, happiness, love | 4 (+4 conflict resolutions) |
| Pa/Eq | liberty†, justice†, community†, individuality†, wealth, reputation, happiness, love | 5 (+3 equity corrections, †) |
| Se/Sl | happiness | 1 |
| R/F | all except honour, stability | 13 |
| G/Hu | all except reputation | 14 |
| D/I | reputation, individuality, happiness, love | 4 |

`happiness` is reasoned 7/7 on a working definition stated in §2.12; `individuality` and `love` 6/7
on working definitions stated in §2.9 and §2.14. Four reasoned cells are **reasoned zeros** (liberty
G/Hu, justice G/Hu, individuality D/I, happiness H/E) — placed at 0 with a reason, not left
unplaced; the grid's other zeros (stability H/E, stability Se/Sl, scholastics Se/Sl, community H/E,
faith H/E, family D/I) are cited or derived and were already there in rev. 1.

### 7.2 Conflicts — resolved to one value in §2 (rev. 2); what each source said

| cell | S1 said | S3 said | rev. 1 primary | **rev. 2 value** | resolution |
|---|---|---|---|---|---|
| virtue × P/S | −0.3 (precedent) | substantive +0.4 | −0.3 | **−0.2** | toward S1, smaller: exemplars (precedent) formed, case (substantive) judged |
| scholastics × P/S | +0.1 (substantive) | memory +0.2 / substantive −0.5 | +0.1 | **−0.1** | **reversed** toward S3: by Jordan's definition the scholar *looks* to the archive first; registry scholastics are archive readers |
| warden × P/S | −0.4 (precedent) | substantive +0.6 | −0.4 | **−0.1** | near-cancel: a continuing practice, substantive in method (Edeyja) |
| justice × P/S | Equity +0.2 (substantive) | +0.6 agrees | +0.2 | **+0.1** | two of three social-justice strands substantive, Baralta's third precedent |
| alignment surveil × D/I | −0.8 | — | null | null (out of scope) | S2's own reason says it is a price, not a pole |
| alignment interview × D/I | −0.3 | — | null | null (out of scope) | same |
| stability × H/E | Order +0.5 / Authority +0.9 | — | 0.0 (S4 ruled) | **0.0** | a ruled departure, not a source conflict |
| faith × H/E, P/S | +0.4, +0.6 | — | 0.0, −0.3 | **0.0, 0.0** (rev. 5) | rev. 2's departure argued at §2.11 and measured at §5.2 arm D; rev. 5 RULED the row magnitude-only (Jordan, 2026-09-27) — P/S, Se/Sl, R/F, G/Hu all 0 |

### 7.3 Cells changed by the equity/equitable correction (Jordan's rule, rev. 2)

The rule, as Jordan restated it in rev. 4: **the ban is on IDENTITY, not on vocabulary.** A
`partisan↔equitable` cell may not be placed by treating the pursuit's content as the same thing as
the pole's name ("justice pursues equity; equity is the equitable pole; therefore high" — circular,
because it gives the pursuit no content the axis does not already have). Describing the pole in
equity vocabulary is fine — it is named `equitable`; and S3's equity-labelled numbers remain
legitimate corroboration. What every Pa/Eq cell must supply is the pursuit's OWN content and an
argument for how that content bears on a disposition of treatment (§1b(c) grounds this: a pursuit is
an END, the pole is a disposition of TREATMENT that any pursuit can carry). Every Pa/Eq cell's
reasoning was rewritten on that shape (for `justice`, the three social-justice strands: distributive
fairness · treatment under law · structural equity in outcomes). **Values changed (4):**

| cell | rev. 1 | rev. 2 | why the value moved |
|---|---|---|---|
| **justice × Pa/Eq** | +0.9 (S3 Equity `equity` 0.9 — the tautology) | **+0.8** | re-grounded on the three strands; reduced because a live partisan flavour of the pursuit exists (Vaynard, Torberg: "justice for my people") |
| **liberty × Pa/Eq** | +0.3 (S3) | **+0.2** | structural-equity strand present (no one placed under another by station) but no distributive programme and, in period sense, the citizen body's freedom — partial to those inside the claim |
| **community × Pa/Eq** | −0.5 (S3) | **−0.3** | distributive fairness is community's content INSIDE the circle; partiality only at the boundary; the registry's community-pursuers are its fairness advocates |
| **individuality × Pa/Eq** | null | **−0.2** | new: indifferent to both strands; the smallest "own side" |

**Reasoning rewritten, value unchanged (7):** virtue +0.3, honour −0.3, scholastics +0.4, stability
+0.4, faith +0.2, family −0.6, warden −0.3 — each now states what fair treatment means for that
pursuit rather than citing S3's `equity` number alone (S3 kept as corroboration). Also re-grounded
without a value change: justice × H/E (+0.4, now argued from strands (a)/(c) against station).
Newly placed on the same substantive ground, not a correction: wealth −0.4, reputation −0.3,
happiness −0.2, love −0.7.

### 7.4 Alignment nulls worth Jordan's eye (§3 is out of rev. 2's scope and unchanged)

- `tell` gets **no cell on any axis** (§3.6); `speak` gets one (G/Hu −0.4). Jordan's Q1 asked about both.
- `kill` / `wound` / `fight` / `challenge` / `accept` carry cells only on D/I, G/Hu, R/F (accept) and
  P/S (challenge) — 9 cells across 35 positions. Their H/E and Pa/Eq are null: nothing in the tree
  says whether a killing engages rank or partiality as a VERB (the candidate's subject does).
- `carry` stays absent on H/E by S2's own refusal.
- `restore` and `thread_read` are unresolvable today (S13 `:509`, `:757`) and carry nothing.

### 7.5 What this file does not do

- It does not touch the five owner files named at the head.
- It does not renormalise any weight vector, bump any `next_free`, or allocate an ED id.
- It does not claim the four resolved conflicts or the 54 reasoned cells are right; it claims every
  one shows its reasoning, so Jordan can strike any of them by reading the row.
- It does not resolve §5.3's correlation defects or §5.2's failed pair; it reports both with the cells
  that cause them and a recommendation Jordan can accept or reject.
