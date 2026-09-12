# Emergent-narrative primitives, v2 — scored on what they do for the game

## Status: **PROPOSED (2026-09-12, ED-IN-0217). HELD BACK FROM RATIFICATION-ON-MERGE, IN FULL.**

⚠ **ED-1094 does not apply to this set, and the exception is stated rather than assumed.** Merging a PR
normally ratifies its `PROPOSED` contents. **Nothing here ratifies on merge.** Every proposal is a design
object for Jordan to accept, amend or refuse.

**Supersedes `proposals/2026-09-12-emergent-narrative-primitives/`** (v1), which remains in the tree as
the audit trail. v1 is not wrong in its facts; it is wrong in its **test**, and the wrong test produced a
set whose largest item was one clause.

---

## §1 · WHY THERE IS A v2 — THE TREE ALREADY RULED ON THIS, AND v1 MISSED IT

Jordan, this session: *"Proposals don't die because of conflicts with existing work. If a proposal is
better, then it must be considered."* Then: *"Even the design commitments are to be ignored if they are
directly attached to code (eg no aggregates on a query)."* And: ***"All we care about is improving the
game."***

**That is `R2`, ratified 2026-09-06, and v1 cited the file it lives in four times without ever quoting
it** (`references/design_rulings_2026-09-06.md:37-50`):

> ## R2 · THE FIVE PROPERTIES — the terminal criteria
>
> *"you have license to do whatever makes for the best game architecture. your only constraints are
> making this as dynamic and capable and flexible and emergent and persistent as possible."*
>
> **Reading.** The ratified refusals become **instrumental, not terminal**. Each must be justified against
> these five or changed. ⚠ But most of them were derived to serve exactly these properties, so a naive
> reading reduces what it means to increase… **The null result — "examined, this refusal earns its place"
> — is a real finding, and must be argued rather than deferred to.**

**The five properties are terminal. Every refusal is instrumental.** v1 deferred to refusals twenty-seven
times and argued none of them against the five. This part of R2 is the whole brief for v2 — including its
caution: R2 is **not** a licence to ignore the refusals, because most were derived to serve these very
properties. It requires each one to be **argued**.

### 1.1 · The grounds, and only one of the three may refuse anything

| | what it is | what it may do to an idea |
|---|---|---|
| **G** | a commitment about **the game** — what the player experiences, whether a narrator exists, what may act, what is shown | **may refuse it** — and must be *argued* against R2's five properties, not cited (§`03`) |
| **A** | a commitment about **architecture** — how state is stored or computed | ⚠ **nothing. A player cannot tell a field from a function** |
| **I** | an **implementation fact** — *"nothing produces it"*, *"no code reads it"*, *"no step exists"* | ⚠ **nothing — this is a cost line, written `I: ~N lines at <site>`** |

### 1.2 · The single misquotation that produced most of v1's refusals

v1's most-used refusal was one sentence of **R7**, quoted in isolation eleven-plus times:
*"no magnitude carrier is admitted at any scale. Every aggregate is DERIVED, none is PUSHED"* (`:169`).

**R7 read whole says the opposite of what v1 used it for** (`:159-195`). It is titled
**"NORMATIVE AGGREGATES PROPAGATE AT THE SPEED OF NEWS ⭐ THE DECISIVE RULING"**; Jordan's ruling was on a
fork between an *echo* model and an *architecture* model, and it then **names the quantities as things the
design HAS**:

> *"The six quantities he named are all Queries… holdings count and military capacity and influence are
> Queries over `hold` and `commit` edges; **legitimacy, the leader's standing and populace morale are
> Queries over `stance`/`convictions`.** So the reason a magnitude carrier feels necessary is that
> **`H-62` is open** — if no stance moves when the army dies, legitimacy cannot fall out of anything."*
>
> *"⚠ **THERE IS NO SINGLE FACTION-LEGITIMACY NUMBER.** It is a field over the population, so **a ruler
> can be wrong about their own standing.**"*

**`legitimacy`, `standing` and `morale` are exactly the corpus's Approval / Standing / Resolve meters, and
R7 admits all three.** What R7 rules is *where the number lives* — an **A** — and it says plainly that a
carrier *feels* necessary only because the **producer** is missing. v1 cited it to refuse the quantities it
licenses. R7 even closes with a yield list that is v1's own `P3`/`P6` proposals, pre-written:

> *propaganda · cover-ups · the intercepted dispatch · the messenger who never arrives · delayed news as
> distance · **rumour vs record graded by `Claim.confidence`, which exists and already decays.***

---

## §2 · THE SET, RANKED BY WHAT IT DOES FOR THE GAME

Ordered by R-WORLD and R-CHOICE yield — **not** by edit size, which is how v1 ordered and is why its best
item was a clause. Full statements in `01_THE_TEN.md`.

| | proposal | what the game can do that it cannot today | `I` cost |
|---|---|---|---|
| **1** | **The chronicle render** — walk `Event.causes[]` and show a person *why* | the player learns that a steward embezzled, a seat changed hands, a term lapsed — **the only way R-WORLD is ever experienced.** §C.11 *obliges* the "why" | a render; the data is already written at every write |
| **2** | **A patron with three pressures** — the Queen's Table as a **person** | one antagonist whose standing, patience and suspicion are Queries over her own interiors, who can be bribed, delayed, burned or killed | rides `H-62`/`W-F` + `P1` |
| **3** | **Embezzlement, which already runs** | a steward skimming a hearth store; discovered by `interview`/`research`; a grievance that travels | ~0 — `transfer` executes 723× and a hearth is a Rung |
| **4** | **Declared terms on tenures** (`T-n`'s unbuilt half) | read the year of your own coup off a term; renew, let lapse, break early | one field + one MATTER branch |
| **5** | **The bodies clock** — ageing, births, deaths on `Rung.envelope` | the one compounding quantity the design licenses without an author: boom, bust, an heir of age, an elder dying and a `hold` ending | `census.py` writes nothing today |
| **6** | **Complication as the modal outcome** | most acts succeed *at a cost* instead of refusing — the hook generator. Measured today: **74% Failure · 19% Partial · 0% Overwhelming** | fixtures are `assumption`; the ladder is Jordan's |
| **7** | **Intelligence before action** | spend acts to learn a rival's state, then act on what you hold — and be wrong | the investigation verbs already run |
| **8** | **A person-referent route** (v1's `P1`, kept) | any act directed at another person: court, discredit, poach, audit | one clause |
| **9** | **Founding** — `Rung.exists` has no producer, and `R4` asked for one | map variation across playthroughs; NPC-founded settlements | one verb; the matrix row is declared |
| **10** | **Casus belli as a `Record`** | a war with a reason others can be told about, forged, or destroyed | `succeed`/`forge` declared |

**Five of the ten are licensed-and-unbuilt**, meaning a ratified line already *asks* for them. Three need
no new object at all. **None requires revising a G.**

---

## §3 · HOW TO READ THIS SUITE

| file | what it holds |
|---|---|
| `00_INDEX.md` | this — `R2`, the `G`/`A`/`I` grounds, the R7 misquotation, the set |
| `01_THE_TEN.md` | the ten proposals, each **agonist → antagonist → reconciliation**, with grounds and an `I` cost |
| `02_THE_RESCORE.md` | v1's twenty-seven dispositions and Part E's seventy-six rows re-scored `G`/`A`/`I`, and the tally re-derived counting **only G** |
| `03_WHAT_SURVIVES_R2.md` | the refusals that hold — each **argued** against the five properties, which is the null result `R2` requires |
| `04_PROVENANCE.md` | method, the two independent read-only audits, every verification run, and what could not be established |

---

## §4 · WHAT IS NOT CLAIMED

- **`H-62`/`W-F` is Jordan's and already planned** to the YAML (`workplans/2026-09-09-r-execution-plan.md:1324`). Proposals 2 and 4 ride it; they do not claim it.
- **`R4`'s four churn routes are Jordan's directive** (`design_rulings_2026-09-06.md:77-87`). Proposals 5 and 9 are two of the four, named as his.
- **The dice ladder is Jordan's**, ruled 2026-08-14. Proposal 6 proposes the *question*, and the fixtures behind it are his tuning.
- **No new `needs_jordan` row is filed.** Proposal 6 surfaces one genuine design call — *should complication be the modal band* — and it attaches to fixtures he already owns.
- **The seven source documents are not in this repository.** They are pinned by SHA-256 in `04_PROVENANCE.md`; every claim *about them* is unverifiable from the tree and marked.
