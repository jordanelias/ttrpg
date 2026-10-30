# Part 3 verdicts — G (outcome, binding, enforcement) · H (transfers) · I (disorder) · K (emergent narrative)

## Status: **REFERENCE (2026-10-29).** Verdicts of fit; continues `2026-10-29-debate-fit-adjudication.md`, whose status, method and limits apply here. Judgments, not tasks.

Adjudicator: Opus, terminal pass. Tree read: `C:\Github\ttrpg-parliament` @ `d90b6e8d`. 241 entries → 26 clusters.
Tiers abbreviated: C = CODED/RATIFIED, I = INTENT, P = PROPOSED/ARCHIVED, R = RESEARCH, H = HISTORICAL/GAME/NARRLIT.
For K clusters N/E/R/S is applied to the REQUIREMENT the literature states; "Narr" is the main test.

## 0. The group's own question — can a motion affect the world, and how hard should it bind?

**Yes, and the right strength is NEGATIVE CONCURRENCE (T3a) plus a WITNESSED held record (T2) — not obligation (T3b).**

1. **What H-90 actually requires.** H-90's verbatim cite (`engine/season/hole_register.yaml:1116-1126`, opened) says *sovereign power is uncontested and absolute … there is a Parliament, so there is no monopoly of power in the ruler*. Canon (`canon/03_canonical_timeline.md:88`, opened): the Crown is *first among equals*, *ducal authority cannot be unilaterally overridden*, and the rebuttable deed-presumption is enforced by *the Coup Counter and Motion of No Confidence*. Every clause is a **denial of unilateral power**, none a grant of positive command to the assembly. T3a satisfies all of it: some acts of the owning seat (confirm a nominee CR-36, strip the throne CR-37, a consent-gated cession) cannot run without a held `resolution`. Canon's named enforcement — no-confidence — is exactly CR-37's `joint_concurrence` revoke. H-90 does not need T3b.
2. **What the history says.** In every enforcement form gathered, an assembly's *positive* force was executed by a person: Reichsacht → Reichsexekution by princes the Diet authorised (HP-041); capitularies deliberated with magnates, *read out by missi* (HP-006, HP-007); Avogadori *suspend or annul* — negative (HP-027); the remonstrance ladder ends in *lit de justice*, the king overriding (CL-040); the Fengbo clerk *refuses to transmit* — negative (HP-063); *senatus auctoritas* binds by standing, not command (HP-002). Promulgation and enforcement were always two parties' acts. The engine already splits them: `issue` mints; `comply` and `evade / defy` (graded `ruled`, emits `compliance.withheld` — opened) are the executor's own acts, both writing `[]`.
3. **Why T3b does not fit.** (a) No gate basis lets a bench open a tenure on a seat (`DISPOSABLE_KINDS`, proposal §6). (b) Obliging the ruler to act makes his *non-act* the breach, and a non-act emits nothing — the ners "silence beats refusal" defect built in. (c) It gives the assembly the monopoly H-90 denies to the ruler.
4. **The defect T2 carries as designed.** The ruler who ignores a held resolution does nothing, so nothing is witnessed. The record only bites if declining is an **act**. The writ machinery already provides one (`defy` → `compliance.withheld`), and so does the remonstrance ladder (each escalation an act). **T2 fits only if the resolution reaches the owner and his answer is an act; as designed, silence dominates.**
5. **What binding hangs on.** CR-36 and CR-37 both deliver the resolution to the executing seat by a `give` (`workplans/valoria_master_workplan_v10_part4.md:382,393`, opened), and a computed `give` of anything but a few Records does not form (H-229, opened). **Today every route from a carried motion to a world change is hand-built.** That is the group's biggest finding.

## 0.1 Land/asset transfer as a social-contest outcome: persons through seats, holding a document

| historical form | expressible? | carrier (verified where marked ✓) |
|---|---|---|
| Cession / gift of land by consent; enfeoffment-by-grant | **yes in shape, inert in play** | `give` on a Rung (✓ `verb_table.yaml:571`): own act, receiver present; 0 computed executions (✓ H-229) |
| Appointment, investiture | **yes** | `confer` through a seat (CODED) |
| Nomination by body + confirmation | **yes, hand-built** | CR-36: `determine` mints `resolution`; confirmer holds it and `confer`s |
| Dismissal | **yes** | `revoke`, rung above, same faction; appointed → permanent ban (✓ `gate.py:590`) |
| Confiscation by writ | **yes — exactly the requested shape** | `seize` Record half needs a **held dispensation naming the Record**, and a seat may license itself by one `issue` (✓ `:1151`) |
| Conquest / occupation | **yes** | `seize` Rung half, licensed by occupation and muster (✓) |
| Deposition by no-confidence | **yes, hand-built** | CR-37: resolution + the Holy See's own `revoke` |
| Forced cession by assembly vote | **expressible in shape, undesigned** | a resolution serving as `seize`'s warrant — CR-37's pattern applied to a Rung |
| Inheritance | **partly** | `succeed` = heir's own claim; row declined today (OP-049) |
| Sale or purchase of title (Visconti) | **no** | the gate's `handover` admits only a non-seat hold: a seat given is `NotYours` (✓ `give` note) |
| Sale of land for price | **no as one deal** | `give` + `exchange` are separate; nothing ties the gift to the terms (proposal §7) |
| Quo warranto, judicial award of a disputed hold | **no** | `determine` cannot dispose a `hold` (H-217, CD-071); `seize`/`revoke` need no hearing |
| Charter of privileges; prescription | **no** | no privilege carrier; every hold minted `since 0`, so age is unreadable (NL-068) |
| Entry charter / dedizione / Charter of Submission | **as a citable Record only** | `covenant` is held by its maker; nothing binds the new holder's later acts |
| Fief as a renewing bond (homage) | **partly** | `give` + `oblige` as two acts; renewal at death not carried |

**Rule that sorts the table:** a form is expressible when it reduces to one person's act whose precondition reads a Record that person holds. It is not when it needs (i) a hearing that disposes a `hold`, (ii) a seat to move as property, or (iii) terms that bind a later act.

## 1. Clusters — G

**G1 · Assembly mints a resolution; an owning seat executes (T1/T2/T3a/T3b) — `FITS-IF-ADAPTED`**
CD-103, CD-063, GV-088, GV-085, HP-002, HP-006, OP-065, HP-005.
- NERS: N holds top-down (throne revocable), bottom-up (members commit) and lateral (Holy See concurs); **fails vertical** (no reach below realm). R-world: a carried, unexecuted motion is a standing grievance. R-complete fails at one extreme: a carried vote can lose on dice (CD-104). S: one count (commits) serves vote and election. E: high — no new verb, one conjunct per row.
- Adaptation: the owner's declining must be an act (writ precedent), and the resolution must reach him by something that forms.
- Narr: NOTCODED. A held, ignored resolution, and a deposed king who keeps his duchy, are strong hooks when no player is present — reachable only by hand-built `give`.
- Persons: the executor chooses; the chooser has no risk or horizon term (K3).
- Fails player: carried, then nothing, with no visible refusal → inert.
- Evidence: C (plan positions, unbuilt) + R. OP-065's rung-scaled rider needs the unbuilt nested run.

**G2 · Writ and compliance (issue / comply / evade-defy; the Word) — `ALREADY-HELD`**
CD-038, GV-065, GV-084, GV-036, HP-063, GV-064.
- NERS: N holds in all six directions — the one top-down channel whose reception is each executor's own act. R-world: every recipient answers differently (GV-084). S: Writ and Word are two transports differing in fidelity, consistent with `tell`. E: high.
- Correction: CD-038's "non-compliance is weak" is wrong. `evade / defy` exists, graded `ruled`, and emits `compliance.withheld`; only `construe` is `absent`.
- Narr: CODED. A defied writ is a witnessed deed others judge. GV-064 (RR-P: the act is inviolate, its reception is not) is this cluster's principle.
- Persons: conviction drives comply vs defy; no risk term yet.
- Fails player: low; delivery of a writ runs through `give` (H-229).
- Evidence: C.

**G3 · Checks on a measure: remonstrance, countersignature, Stay, annulment — `FITS-IF-ADAPTED`**
CL-040, HP-063, GV-073, HP-027, GV-006, GV-076 (Stay half).
- Adaptation: each check is a person's **act** (refuse to transmit, defy, an appeal-`determine` on a prior resolution), never a Stay status or a PI band.
- NERS: N holds lateral (a peer body checks the ruler), the direction G1 lacks. R-world: an escalation ladder generates sequences with no director. S: the archived Stay suspended a transfer "pending external resolution", a clock-shaped state that AX-5 refuses (PR-047). E: worse if built as a state, neutral if built as acts.
- Narr: NOTCODED except defy. The remonstrance ladder is the best non-violent escalation story in the corpus.
- Persons: the remonstrant risks his career (HP-063 asks for a personal risk roll), which needs the absent risk term.
- Fails player: built as a free veto → dominant obstruction.
- Evidence: R/H only; the Stay code was deleted (GV-060).

**G4 · Offices: conferral and revocation bases, disposal, remit legibility — `ALREADY-HELD`**
GV-049, GV-050, GV-063, CD-041, GV-048, GV-051, GV-062, OP-108, GV-097, GV-101, GV-102.
- NERS: N holds top-down; **fails bottom-up** — removal by an assembly's vote waits on CR-37, and an elected seat has no count (GV-097). R-complete fails at the extremes: no duchy is in the monarch's holdings, so no duke is strippable (GV-049), and 14 seats are revocation-null. S: one basis set (appointed / elected / annex) prices consistently. E: high.
- Narr: CODED. The ban on a dismissed appointee is a lifelong grievance. OP-109: null-conferral seats emptied at tick 0 never refill — **dead seats**.
- Fails player: H-71's other half is open (GV-102), so "was he entitled to act?" cannot be contested.
- Evidence: C.

**G5 · A disposal must write something somebody can lose (ABOUT the world) — `ALREADY-HELD` as a test**
PR-073, PR-016, PR-040, PR-047, NL-047, NL-031, HP-102.
- NERS: this is the churn principle made testable, so N holds by definition. Its refusals — no stakes internal to the room, no self-executing verdict, no verdict as shared fact — match the no-GM, per-ledger axioms. E: it is a test, not an object.
- Narr: CODED for tenure disposals (detain, ban, oblige); the Record disposal is NOTCODED (B-2). It excludes both failure poles: EU4 estates that never fire (HP-102), and the old bridge that fired a subjectless motion every season.
- Evidence: I (Jordan ruling) + C.

**G6 · Disposal reach / announcement — `HELD-FOR-REASON`**
PR-020, PR-030, NL-050, CD-010, NL-108.
- Prerequisite missing: the `<rung kind>` reach channel. `disposal_reach` and `term_required` have no reader beyond the loader (verified), and the chronicle channel matches nobody.
- Narr: until it exists a sub-realm resolution reaches nobody outside the room, which fails NL-108 (losing the one point that delivered the information). The split between who argued and who learns is the right design.
- Evidence: I + C (absence verified).

**G7 · Appeal, release, closure, contumacy — `PARTIAL`**
PR-009, PR-044, PR-055, PR-098, GV-028, PR-039, PR-109, OP-020.
- Fits the tenure layer: `release` is coded and absorbs repudiate, so a vow-break is a priced, witnessed deed (PR-098), and AX-6 (what opens can close) holds. **Does not yet fit proceedings**: `appeal_basis` is unread, and contumacy as a finding is unbuilt.
- NERS: R-complete — the indefinite inquisition (PR-039) stays contestable because whoever set it can be reached. S: the depth cap is declared by the opening act, not a default constant.
- Persons: reversing a vote openly costs reputation, which persons with different convictions pay differently.
- Evidence: C + I.

**G8 · Archived sanction ladder and motion catalogue (stat deltas) — `MISFIT`**
GV-010, GV-011, GV-012, HP-082, OP-010, OP-014, OP-015, GV-076, HP-041, OP-085, GV-046.
- Misfit against hard constraints: factions propose and suffer (Mandate −2, Stability −1), yet a faction never acts; penalties are stored gauges, not things anyone can lose; durations are clocks (AX-5).
- What survives: the motion **kinds** (censure, outlawry, subsidy, succession endorsement), as rows naming a strain query and an executing verb (proposal §3). That is the adapted form, not this one.
- OP-085's finding — intermediate branch points are what make governance feel alive — stands, and argues against terminal transfers.
- Evidence: P/R; all of it retired code.

**G9 · Oversight: missi, Avogadori, inspection, suspicion, hostage-kin, promissione — `PARTIAL`**
HP-007, HP-066, HP-067, HP-024, GV-027, GV-042, HP-026, HP-016.
- Fits as **persons who travel and tell**: a missus is a `tell`/`examine` carrier whose pair keeps independent ledgers. HP-067 (certainty of detection weighs as much as severity) is the engine's non-total fan-out read as policy.
- Misfit as the sources state them: suspicion tracks and accrual counters are stored gauges, and "two audit channels concur → demotion" is a threshold firing an outcome, which T-b refuses.
- Evidence: H/R only — a tier-3 verdict.

**G10 · Oaths and performative binding — `ALREADY-HELD`**
HP-009, CL-067, CL-068, HP-024 (oath half), PR-098.
- `oblige` and `commit` are oaths: own acts, closable only by the swearer's priced `release`. Supplication (CL-067) binds the powerful through the cost of a public refusal, which is reception of a witnessed `petition` (coded).
- Misfit residue: a kishomon oath form that escalates with "world trust" needs a world-trust state (a forbidden world condition); a population-wide oath as a legitimacy reservoir is a gauge.
- Evidence: C for the carrier, H for the forms.

**G11 · Consent cascade; legitimacy as soft power — `FITS-IF-ADAPTED`**
GV-030, GV-033, HP-029, HP-002, GV-098, HP-005, HP-019.
- Adaptation: legitimacy is computed when read, from persons' ledgers (`legitimacy`, `person_q.py:452`), never an L/PS gauge modulating a cascade.
- NERS: N holds bottom-up — the one route by which settlements constrain a duke without arms. S: the archived L/PS was inert in its own sim (GV-030's note).
- Augustus accreting powers and Visconti buying a title (HP-005, HP-019) need a seat to be sold, which the gate refuses: not expressible.
- Evidence: C (canon) + P.

## 2. Clusters — H

**H1 · `give`: consensual transfer of land or a Record — `PARTIAL` (shape held, inert in play)**
CD-039, HP-069 (delivery half).
- NERS: N holds at every seam — the only consensual route for title, and the delivery route for every resolution, warrant and challenge. R-complete **fails**: 0 Rung cessions in 143 worlds (H-229, opened). S: one verb for documents and land. E: high.
- Narr: NOTCODED in effect. A treaty cession, a dowry, land as a bribe all need it.
- Fails player: the player can give, but no NPC ever gives back → one-directional (a churn violation).
- Evidence: C.

**H2 · `seize`: confiscation by a seat holding a warrant — `ALREADY-HELD`; quo warranto `HELD-FOR-REASON`**
CD-040, GV-039 (hearing half), GV-106.
- Verification widened the entry: the Record half requires a **held dispensation naming the Record**, and the Rung half licenses on occupation and muster — exactly "a person acting through a seat, holding a document".
- Missing: any hearing before a seizure. Quo warranto needs `determine` to dispose a `hold` (H-217).
- Narr: CODED; a seizure emits `rung.seized`/`record.seized` to the seat's obligees.
- Fails player: a seat can license itself with one `issue`, so confiscation is cheap and only reception prices it.
- Evidence: C.

**H3 · Charters, entry terms, dedizione, recognition fork, Serrata — `HELD-FOR-REASON`**
GV-039, GV-040, HP-046, HP-069, HP-104, GV-026, HP-023.
- Prerequisites: a carrier for terms that bind a later act (privileges), and a readable hold age (prescription). Neither exists; every hold is `since 0`.
- If built, N is high: "conquest should produce a negotiation, not a colour change" (HP-069). The confirm-vs-new-grant fork (GV-026) needs no gauge and fits now, as a choice between `confer` and not acting.
- Evidence: P/H; HP-104's own companion flags its overconfidence.

**H4 · Parliamentary territory transfer; casus belli ledger — `MISFIT` in source form**
GV-001, GV-002, GV-003, GV-004, GV-034, GV-035, GV-071, OP-107, OP-047, OP-058.
- Misfit: a faction's Influence rolls against a faction's Legitimacy, and the body writes the transfer — breaking "only persons act" and "the assembly never acts".
- What survives: (a) the transfer, expressed as resolution + `seize` warrant or + the holder's own `give` (§0.1); (b) casus belli as a **Record others can be told about, forge or destroy** (OP-107), with `declare` writing the declarer's own commit (OP-058). Both fit. The 3-season CB lifetime is an unsourced default.
- Evidence: P (archived) + I for OP-107.

**H5 · Succession and deposition — `FITS` (CR-37) / `HELD-FOR-REASON` (contested succession)**
OP-049, GV-077, OP-013, CD-071, GV-079, GV-074, GV-075, OP-086, OP-072, OP-109.
- CR-37 fits: two persons' acts, no threshold, and the deposed king keeps his duchy, so he lives on as a rival. The heir's claim as his own act fits. GV-074's PI meter and GV-075's conjunction-fired deposition **misfit** (T-b: a threshold may only raise a question, NL-081).
- Contested succession waits on H-217 (no succession arrangement, no hold disposal; CD-071).
- Narr: OP-072 (a Crown claim composed from two contested successions, nothing authored) is the model hook. OP-109 shows the cost of the gap: the throne empties at tick 0 and never refills. **[Unreproduced: the "tick 0, every seed" reading comes from an uncommitted probe at `51d7b05`; H-230 cites the King dying in season 1 at seeds 0 and 2 on base `c6459377`; a four-season run on `120b3bf7` finds him alive at seeds 0 and 2. Three bases, none reproducible from the tree. See `2026-10-29-resolution-design.md` §2A.]**
- Evidence: C (plan) + P.

## 3. Clusters — I

**I1 · How a motion ends: lapse, deadlock, obstruction, silence, dice after the vote — `FITS-IF-ADAPTED`**
CD-100, CD-070, CD-104, OP-012, HP-059, PR-078, HP-106, HP-060.
- Adaptation: one end, a witnessed lapse at MATTER (CD-100). CD-104 is a completeness failure — the count already decided, yet a roll can undo it.
- NERS: R-complete fails today (a below-quorum motion retries forever). PR-078 prices silence with no event and nothing anyone can reconstruct — an invisible cost, misfit. HP-059 (consuming the session clock) needs scarce slots a season-granular sitting lacks — misfit now. Victoria 3's enactment stages (HP-060) are a clock — misfit. The liberum veto (HP-106) is a name only — **cannot judge**.
- Evidence: C for the defect, R/H for the rest.

**I2 · Collision of stresses, channel starvation, relief valves — `FITS-IF-ADAPTED`**
HP-034, HP-035, HP-036, HP-033, HP-038, HP-020, HP-021, CD-045, OP-095.
- Adaptation (proposal §3 already takes it): strain from an existing query, plus an independent trigger of **another claim kind**, raises a question — never fires a revolt.
- NERS: N holds bottom-up and diagonal (material strain × legitimating utterance). HP-035 is an R-world argument *for* a parliament: with no contest channel, grievance exits as assassination — N for the whole subsystem. CD-045's revolt query takes no petition and accumulates nothing — a portrait.
- Evidence: R/H + I (T-b).

## 4. Clusters — K (what narrative theory requires)

**K1 · A story needs a difference between ledgers plus a want — `ALREADY-HELD` (mostly)**
NL-052, PR-085, NL-111, NL-053, NL-054, NL-090, NL-063, NL-042, NL-056, NL-057, NL-058.
- Narr (main test): of the eight mechanisms, six are CODED, two of them partly — non-total fan-out, attribution, told_by, reception read from ledgers, pressure crossings, conviction moved by consequence (restabilise unbuilt). The summons return day is half-present (`Tenure.term`). The unmet-want term is NOTCODED, though the ambition question fires (NL-057). Telling is rare (11 tellings in two seasons). The substrate for "the wrong man blamed, the rumour believed by the bench" exists, but has never been measured in a sitting.
- NERS of the requirement: N holds (without a difference there is only a log). S: one ledger per person and no shared transcript, consistent with PR-047.
- Evidence: C.

**K2 · Memory must be read at a decision point (a recorded defeat inside a later vote) — `FITS-IF-ADAPTED`**
NL-060, NL-062, NL-094, NL-096, PR-088, PR-089, PR-090, PR-092, NL-088, NL-089, OP-073.
- Requirement: memory gates **eligibility or a choice**, not mood. Met for regard, which enters the stance term. Failed for motions: a voter cannot see what a motion says, so every `commit` scores the same (proposal §5).
- Adaptation: one reader of the motion's content against the voter's own pursuits and the party's standing — CK's "show the causally relevant subset", not more summed axes (NL-088 calls the convictions matrix "a smaller Prom Week"). Nemesis-style re-scheduling (NL-094) is a director, and misfits.
- Evidence: H (GAME), with C confirming the gap.

**K3 · Persons differ in risk, horizon and conviction; non-rational choice — `HELD-FOR-REASON`**
NL-032, NL-033, NL-084, NL-055.
- Prerequisite: CR-17 (believed odds weight the alignment term). `score_terms` has three terms (verified, `choose.py:130`); ties break alphabetically; scars ship at shift 0.
- Narr: under argmax a division is uniform — votes with no hooks (NL-084). This blocks the "Persons" line of nearly every G and H cluster.
- Evidence: C for the absence; a RATIFIED ruling for the want.

**K4 · Initiation without a deck or director: occasions, outside pressure, emergence — `FITS-IF-ADAPTED`**
NL-079, NL-068, NL-080, NL-048, NL-081, GV-103, GV-078, NL-005, NL-028, NL-029, NL-007, NL-097.
- Requirement (Aylett, NL-005): enough events outside the characters' control. The repo: outside forcing is off by default (NL-080), and a world where nobody convenes has no proceedings (NL-048). The occasion ladder — existing questions, then authored boot rows, with a per-season emitter refused — meets the requirement without a director.
- GV-103's Pi homeostat is rubber-banding: misfit. GV-078 (new voices enter by emergence, admitted by `oblige`) fits.
- NL-097's GM functions: chair, caller and deadlock-breaker are carried (Speaker, `convene`, lapse); the pacer is dropped.
- Evidence: I + H.

**K5 · No steering; curate outside the simulation — `ALREADY-HELD` (as constraint)**
NL-040, NL-066, NL-076, NL-008, NL-012, NL-027, NL-099, NL-038, NL-039, NL-078, NL-037, NL-044, NL-046.
- The literature splits (NL-099); the repo has chosen. `choose` sees no World (R-07), thresholds only raise questions (T-b), and sequences may be scripted but arcs may not. Façade-style managers and AI directors misfit; the toy evidence agrees at low confidence (NL-076).
- Conflict to flag: the ratified forecast field and Light Function (NL-038/039) against the proposed refusal of any stored salience field (NL-066). Both are unbuilt, so no code is contradicted.
- Evidence: C (structural) + H.

**K6 · Off-stage delivery, focalized journal, retelling, indexical traces — `FITS-IF-ADAPTED`**
NL-006, NL-045, NL-064, NL-093, NL-069, NL-070, NL-091, NL-002, NL-014, NL-015, NL-016, NL-104, NL-108.
- Requirement: a sitting the player missed reaches him diegetically (gossip, document, returning member), with sources and staleness. Adaptation: a per-person projection, never a World (NL-093), and a content-bearing Said record (NL-091) as the minute-book.
- Fits the per-ledger design: contradicting claims are told side by side, never reconciled (NL-069). But 112 of 120 Records carry no content, so a minute-book would have nothing to say today.
- Evidence: P + H.

**K7 · Instruments: chronicle, story-bar, arc reader, sifting, endings — `FITS` as instruments; terminus `HELD-FOR-REASON`**
NL-071, NL-072, NL-073, NL-082, NL-067, NL-020, NL-021, NL-022, NL-098, CD-093, NL-107, NL-036, NL-035, NL-075, NL-083, NL-110, NL-077, NL-065, NL-049.
- CODED observers that write nothing. Sifting outside the loop is the remedy the literature recommends (NL-024). CD-093's bout classifier is unadopted and its thresholds are eyeballed.
- They show: R-01 propagation met; 76% of acts refused; closers rarely execute; no ending reachable (H-176).
- Evidence: C.

**K8 · Legibility, small cast, agency, dominance — `FITS` as requirement; engine `PARTIAL`**
NL-025, NL-026, NL-013, NL-101, NL-100, OP-094, NL-095, NL-010, NL-009, NL-001, NL-003, NL-004, NL-017, NL-018, NL-019, NL-043, OP-051, OP-056, NL-109, NL-023, NL-024, CL-050.
- Requirements: a small, named bench (NL-025); every surfaced trait is an input to some decision (NL-013); a verb with no model behind it is false agency (NL-010). Today `speak` writes nothing and `argue` never executes in computed play (OP-051). Ludonarrative dissonance (NL-100) applies directly: a text that calls a vote binding while nothing executes it.
- CL-050's route-forcing dominance cannot be judged without the nested run. OP-094 (every number visible) collides with NL-043 (hidden, load-bearing inputs); the corpus leaves this unresolved.
- Evidence: H, with C showing the gaps.

## 5. Ranking by fit for purpose (best first)

1 **K1** (coded drama substrate) · 2 **G2** (two persons' acts) · 3 **G5** (churn made testable) · 4 **G1** (right binding; delivery and silent refusal hold it back) · 5 **G4** (coded; dead seats at extremes) · 6 **H2** (already the requested shape; no hearing) · 7 **I1** (cheap completeness fix that leaves a hook) · 8 **H5** (canon's named enforcement) · 9 **I2** (question-raising, lawful) · 10 **K2** (debate's most visible failure) · 11 **G10** (held by oblige/commit/release) · 12 **K5** (settled constraint) · 13 **K4** (outside events, no director) · 14 **H1** (necessary everywhere, inert) · 15 **K3** (ruled, blocked on CR-17) · 16 **G3** (missing lateral; tier-3 only) · 17 **G7** (tenures only) · 18 **K6** (Records carry no content) · 19 **G6** (no channel) · 20 **K7** (outside the game) · 21 **K8** (engine mostly fails it) · 22 **H3** (no carrier) · 23 **G9** (gauges in source) · 24 **G11** (only as computed legitimacy) · 25 **H4** (factions act) · 26 **G8** (stat deltas on factions).

## 6. The clusters that most affect the others

- **H1 `give`** — the hinge of the group. CR-36, CR-37, a resolution used as a `seize` warrant, E's completable negotiation (PD-5) and writ delivery (G2) all deliver by `give`. While H-229 holds, all of them are hand-built.
- **G1 binding** — leans on D (CR-34's count of live commits; the declared `determine` that still rolls) and on B (the council as one seat by `oblige`, CD-043/GV-061/CD-097). It **collides with C**: `argue` ignores the motion's content (proposal §5), so T1 is empty, and a vote cannot be moved *on this subject*.
- **K2 + K3 (memory at a decision point; persons differ)** — they decide whether D's divisions differ at all. They lean on M (persons as inputs) and C (reception), and collide with F: no side payment reaches a `commit`, so no vote can be bought.
- **I1 lapse** — leans on A (a motion question ranks below every `need`; CD-098) and B's docket (CD-020); it repairs G1's silence at room level.
- **G6 reach** — J and K6 assume a disposal travels; nothing carries it past the room.

## 7. Verification (sources opened in `C:\Github\ttrpg-parliament`)

| entry | opened | result |
|---|---|---|
| CD-039 `give` / H-229 | `verb_table.yaml:571`; `hole_register.yaml:4802` | **Held.** Rung `give`: 0 executions in 143 worlds. Added: `handover` admits only a non-seat hold, so a title cannot be given or sold |
| CD-040 `seize` | `verb_table.yaml:1151` | **Held, but incomplete.** No bench or hearing, true; omitted: the Record half needs a held dispensation naming it (a self-issued warrant suffices), and the Rung half licenses on occupation and muster |
| GV-050 `REVOCATION_DISPOSAL` | `state/gate.py:583-597` | **Held verbatim** (appointed → ban; elected/annex/None → nothing) |
| CD-063 / GV-088 CR-36, CR-37 | `workplans/valoria_master_workplan_v10_part4.md:378-402` | **Held.** Hand-built only; delivery by hand-built `give`; no computed route until H-80 |
| GV-098 canon | `canon/03_canonical_timeline.md:88-92` | **Held**, and stronger: canon names the Coup Counter and the Motion of No Confidence as the enforcement mechanisms |
| H-90 (via GV-058 / CD-109) | `hole_register.yaml:1116-1126` | **Held.** It also records PARLIAMENT, SOVEREIGN POWER and DELEGATION as unbuilt |
| NL-050 / CD-010 | grep of `engine`, `modules` for `disposal_reach`, `term_required` | **Held.** Only `data/arrangements.py` (the loader) and a comment at `effects_information.py:597` |
| NL-033 | `decision/choose.py:130-150` | **Held.** Three terms: pursuit, stance, urgency |
| CD-038 | verb list; the `evade / defy` row | **Wrong in part.** `evade / defy` exists, `ruled`, emits `compliance.withheld`; only `construe` is `absent` |

**Where the corpus is thin (a finding):** the Sejm and the liberum veto are names only; enfeoffment as a renewing bond, quo warranto's procedure, and the Avogadori rest on one research file each (tier 3); no entry in this group measures a sitting in computed play.

