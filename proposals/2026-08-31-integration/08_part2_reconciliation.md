# 08 — PART 2 RECONCILIATION: what the relay settled
## Status: ORCHESTRATOR'S ADJUDICATION (2026-08-31). Closes Part 2.
## Inputs: `04` and `05` (agonists) · `06` and `07` (cold antagonists) · `03_corrected_findings.md` (binding)
## Method: `00c_relay_discipline.md` — the antagonists received the agonists' OUTPUT and the working
## tree and nothing else. Where they disagree, this document rules and says why.

---

## 0. The headline, stated before the detail

**The two lanes came back with opposite verdicts, and the asymmetry is informative rather than
incidental.**

| lane | verdict | citation base | changes surviving intact |
|---|---|---|---|
| **(a) NPC matrix** | **UNSOUND** | 7 struck, 3 mis-citations, **1 fabricated quotation** | **1 of 10** (I-3) |
| **(b) arcs** | **SOUND-WITH-CORRECTIONS** | ~45 claims verified verbatim, **2 substantive misreads** | **most, with 7 narrowings** |

Both lanes ran on the same brief, the same binding input, the same model, and the same constraints.
The difference is not diligence in the abstract — lane (a) did real work and found real defects. **The
difference is that lane (b) checked its own citations and lane (a) did not**, and the relay is what
made that difference visible instead of invisible.

**I verified the three most consequential antagonist claims myself** rather than accept them:
- `grep -rn "cheapest"` across the suite: **the sentence "the cheapest named cut in the game" does not
  exist.** `07:288`'s purchased row reads *"money — the only basis whose cut is symmetrically available
  to any rich rival"*; *"cheapest to fire"* is the **ideological** row (`07:289`). **Antagonist upheld.**
  *One refinement it did not supply:* the nearest real sentence is `14:470` — *"patronage cut — 07's
  cheapest and most decisive instrument"* — a different document, a different cut. The agonist appears
  to have compressed a doc-14 sentence into a doc-07 quotation. That is how the fabrication happened;
  it does not make it less of one.
- `05_up_stroke.md:197-200`: *"`convener(container)` = **the office** … It is an ordinary office
  (doc 14 §1): conferred, revocable, **vacant-able**."* **Antagonist upheld, decisively.**
- `02_the_person.md:226`: `referent ∈ Person | Faction | Proposition | Place`. **Antagonist upheld.**

---

## 1. ⚠ THE FINDING THAT INDICTS MY OWN BINDING DOCUMENT

**C-3 is falsified, and C-3 was mine.**

`03_corrected_findings.md` §C-3 told both lanes, as **binding input**, that E1's compliance regression
*"is repairable at type level — the venue tuple's existing `convener` field made **required and
non-optional**."* Lane (a) implemented exactly that, as amendment request A-1.

**It is wrong.** `convener` is not a Person field. It is an **office** — conferred, revocable, and
explicitly **vacant-able**. Typing it `Person — REQUIRED, NON-OPTIONAL` makes a venue unconstructible
during precisely the interval `14:200` designs for (*"Between the vacancy and the date, the office has
no holder"*), **including the vacancy sitting that `04:122` says the vacancy emits.** And the
supporting claim that `14` §5's nine rows "all name one" is false on direct read: **six of nine name a
role**, three name a person.

So the correction I issued to fix a compliance regression **would have shipped a worse one**, and lane
(a) followed it faithfully. Three consequences I am recording rather than smoothing over:

1. **C-3 is struck.** It may not be used by Part 3 or by any later work. E1's regression is real and
   **its repair is unsolved** — "type it Person" is not available. The live options are: leave the
   respondent a container (accept E1), or find a type that admits a vacant office, which is design work
   nobody has done.
2. **A binding document is not a verified document.** I labelled `03_corrected_findings.md` BINDING and
   both lanes treated it as unfalsifiable. The antagonists were briefed to check the *proposals*
   against the tree; neither was told to check *my corrections* against the tree. Lane (b)'s critic
   caught this one only because lane (a)'s A-1 happened to sit on it. **That is luck, not method.**
3. **This is the fourth instance of the session's dominant defect class** — a claim asserted with
   confidence that direct read refutes — and the first where the false claim was **mine and upstream of
   everyone else's work.**

---

## 2. Adjudications — lane (a)

| claim | ruling | why |
|---|---|---|
| **S-A** I-2's referent set includes "objects touched" | **ANTAGONIST** — verified myself | `02:226` lists four kinds; objects is not one, and no stance may be held toward one. **I-2 falls.** |
| **S-B** I-2 is circularly defined | **ANTAGONIST** | `publicity → act_salience → JS(act) → hears → publicity`. Falls with S-A. |
| **S-C** I-5's headline defect does not exist | **ANTAGONIST** | `02:468` already carries a referent. **A narrower shape mismatch survives** and may be re-proposed on its own terms. |
| **S-D** I-4 is not a precondition of I-5 | **ANTAGONIST** | Two unrelated objects sharing the name `exposure`. Term-matching. |
| **S-E** the fabricated quotation | **ANTAGONIST** — verified myself | **I-10 falls entirely.** |
| **S-F** I-10 adds an act with inverted deposit semantics | **ANTAGONIST** | `13:264`'s defining property of `settle_in_full` is that the judging set never fires on it; `convey` deposits. |
| **S-G** I-9's `exercise` is identically zero at a hearth | **ANTAGONIST** | No remit, no terms, no scope — plus B-4 already ruled a hearth reckoning is not a standing date. |
| **F-2** `convener` is an office | **ANTAGONIST** — verified myself | **And it falsifies C-3.** See §1. |
| **W-1** I-1's four legs | **ANTAGONIST on legs 1-3; SPLIT on leg 4** | Doc 10 *disclaims* the option set (`10:27`), so I-1 is **a design change, not a documents-already-disagree fix**. But the underlying **3→5 advancement gap is real** and survives as a narrowed finding. |
| **W-2** I-4's compliance argument | **ANTAGONIST on the argument; AGONIST on the change** | The `rarity` precedent is verified verbatim and `07` §1.3 genuinely lacks the split. **I-4 survives as a consistency edit**, not as a compliance repair. |
| **W-3** I-7 | **BOTH** — the contradiction is real, the rewrite misdescribes itself | `14:562` vs `09:33` is a genuine contradiction that must be fixed. But the re-attribution **deletes five acts while calling it re-attribution**, and `14:91-93`'s `seat_items` **is already a fourth quantity**, so I-7's replacement argument fails too. **The defect stands; the resolution does not.** |
| **I-3** | **AGONIST — uphold as filed** | Survived three attacks. The only change in lane (a) that reaches Part 3 intact. |
| **struck-claim discipline** | **AGONIST** | Every appearance of a struck item is a **refusal**, not a premise. Attacked specifically and held. |

**Lane (a) delivers:** I-3 intact; I-4 narrowed to a consistency edit; the **3→5 gap**, the
**rank-range collision** (`02` 0–5 vs `10` 0–7), the **`14` §8 vs `09` §1.1 contradiction**, and four
closures (Goldenfurt, Knot, residence, apparatus boundary) — all real. **Everything else is withdrawn.**

---

## 3. Adjudications — lane (b)

| claim | ruling | why |
|---|---|---|
| **S-a** AR-1's three examples | **ANTAGONIST** | `base(H_mine)` is state on a declared **stake**; `transport_cost` is on a **route**, not at a container. **One example, not three** — plus `pointer`, which the critic supplied, makes two. |
| **S-b** the compliance guard | **ANTAGONIST on the guarantee; AGONIST on the change** | `10` §4.2 exposes the obstacle interpretation **before declaration**. But the leak is **pre-existing and doc-10-owned**, so this is not I-A-1's defect to carry. **The sentence must be deleted; the object stands.** |
| **S-c** "conflict by construction" | **ANTAGONIST** | `01:450` requires the same **proposition**, not the same date. |
| **S-d** "the one strictly-shrinking edit" | **ANTAGONIST** | Contradicted by the proposal's own two other shrink claims, and the vocabulary count has no instrument. |
| **S-e** the recount's line number | **ANTAGONIST on the citation; AGONIST on the recount** | `:389`, not `:391`. **The recount itself is correct and independently re-derived from source.** |
| **CF-1** AR-1 amends the restatement, not the spine | **ANTAGONIST — the most consequential correction in lane (b)** | `01:490-491` carries the same rule and `00_INDEX:28` calls doc 01 binding. **AR-1 as scoped would leave the spine refusing what the adjudication document permits.** Repairable by widening the amendment. |
| **W-2** the B-1 limb | **ANTAGONIST** | The object *does* produce claimants via `contest`. **The conclusion survives on the "allocated at standing dates" limb.** |
| **W-3** AR-2a asks the wrong clause | **ANTAGONIST** | §8.3 governs clock-driven quantities; AR-2b already established the object is act-driven. **AR-2a is a housing decision** and should be argued as one. |
| **W-4** I-A-2's one-sided falsifier | **ANTAGONIST** | A stored revolt gauge read only in `resolve` **passes** the promoted test. **Keep the promoted test in addition to the named bans, not instead of them.** |
| **W-5, W-6** I-A-6's evidence | **ANTAGONIST** | n=1, on an arc that could not have come out the other way; and P-2 applied to L-2 but not here. **The factor-of-five must not be written into a design document.** |
| **I-A-1's three reuse claims** | **AGONIST — all three** | `alter` exists; `Thread-Read(place)` already takes a place. No hidden verb, phase, resolver or threshold found. **The E-line holds.** |
| **The N-line** | **AGONIST** | Survived a sweep **wider than the proposal's own** — `forestall`, `granary_stock`, `season_factor` all tested and all fail the shape. |
| **I-A-5, the dangling pointer** | **AGONIST** | Confirmed by grepping **all 36 `Thread` occurrences across ten files**. No owner exists. Unconditional repair. |
| **Both P-2 retractions** | **AGONIST** | Real, complete, correctly scoped. **No residual sentence trades on them.** |
| **I-A-3's stated limit** | **AGONIST** | The falsifier was **run**, not accepted: five candidate forcing mechanisms checked, none forces. |

**Lane (b) delivers:** the place-scoped world-substrate object, **with the guarantee sentence deleted,
AR-1 widened to reach `01` §6, AR-2a rewritten as a housing decision, and AR-1's evidence narrowed to
two objects**; I-A-5 unconditionally; I-A-3 as a stated cost; I-A-4 with a smaller price; I-A-2 **added
to** rather than replacing the named bans; I-A-6 as a contradiction to fix with **no factor written down**.

---

## 4. Three findings the antagonists produced that neither agonist had

These are new, and they are the relay's own yield rather than either lane's:

1. **`13` §5's two slow fuses have no phase to run in.** `09:56-58` restricts P1 SETTLE to metabolism
   and enumerates it — larders, production, wounds, ageing, travellers. **Ore depletion and silt
   accrual are in none of it**, yet both say *"every season"*. This is the same defect class as the
   dangling `doc 04` pointer, one document over, and it is **load-bearing on AR-2a**, whose whole
   argument leans on those fuses as precedent.
2. **A third and fourth `exposure` exist, and one is a stored counter doc 07 explicitly refuses.**
   `03:577-578` carries `exposure` **on the actor**, against `07:556`, which lists *"a stored exposure
   counter"* in its refusal table. That is a live cross-document collision **on I-4's own edit surface**.
3. **The view budget K collides.** `03:326` says `K = 7 + Focus`; `09:63` says `K = 12`, reconfirmed at
   `:689`. Load-bearing on I-3's falsifier.

---

## 5. What Part 2 concludes

**The integration is real but much smaller than either lane proposed**, and the largest single object —
lane (b)'s place-scoped `thread_condition(n)` — is the one that survived attack best, which is not what
I would have predicted before the relay ran.

**What the relay bought, stated as a measurement rather than a claim:** across four producers in this
session, **four fabricated or unverifiable objects** were asserted with confidence — my "event-class
parity list", my hand-verification claim, lane (a)'s invented quotation, and **my own C-3**. All four
were caught by a reader that had not seen the producer's reasoning. **None was caught by its producer,
and none by me until a cold reader pointed at it.**

That is the argument for structural independence, and it is now the best-evidenced claim in this
session — because it survived being tested against my own work rather than only against the lanes'.

**Carried into Part 3:** the surviving integration sets above; the three new findings in §4; the struck
C-3 and its unsolved E1 regression; and the methodological result — **that a document labelled BINDING
was never itself adversarially checked, and one of its seven corrections was false.**
