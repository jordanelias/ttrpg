# 05 · THE ORDER — an AMENDMENT, not a fourth order

## Status: **PROPOSED (2026-09-18). HELD BACK IN FULL. NOTHING RATIFIES ON MERGE.**
## Lane: `IN` · **`ED-IN-0252`**
## Grade under `CLAUDE.md` §0.2: **`paper`.** Nothing in this file has run. Every row names what would run it.
## ⚠⚠ **FOLDED IN AND SPENT AS AN ORDER, 2026-09-18 (`ED-IN-0253`), hours after it was written.** All
## eight rows below now live in `workplans/2026-09-18-governance-settlement-behaviour-plan.md` §3, which is the single
## plan. **Read them there, not here.** Two placements were CORRECTED in the fold: the conviction items
## sat at `24a`–`24c` under SE-BUILD, which was wrong — they are position **12**'s siblings (`12b`,
## `12c`, `12d`), because position 12 is the `Person`-interior writers; and this file's `13c` is just
## position **13b**, which already IS H-71. **The corrections are the argument for one plan**: a
## seventh order surface mis-filed its own rows within a day of writing them.
## What this file still owns: §3's re-pricing of 6b, §4's three collisions, §5's `R-08` correction and
## §6's `ED-SE-0051` finding — reasoning, not sequence.

---

## §1 · WHAT THIS AMENDS, AND WHY AN AMENDMENT WAS NEEDED

`proposals/2026-09-17-governance-and-behaviour/01_THE_BUILD_ORDER.md` says it in its own preamble:
**the 2026-09-17 rulings opened work that order does not schedule.** It scheduled r2's items and the
rulings arrived after it was written. The reconciled program predates both. So there is a set of
**ruled, unblocked, unscheduled** items sitting between two orders, and that set is this file.

**Every row below is ruled or unblocked already.** Nothing here asks for a new design decision except
where the row says so explicitly.

## §2 · THE AMENDMENT — eight rows

| # | handle | lane | what runs | `engine/season/` target | falsifier |
|---|---|---|---|---|---|
| **13c** | **H-71-REMIT** | IN | `person_side_eligible` reads the `hold` Tenure's `payload` instead of declining every `remit:` alternative unconditionally | the eligibility site | `test_no_person_can_choose_a_governance_verb_and_h71_is_why` goes RED the day the hole closes |
| **19c** | **MIGRATE** | IN/SE | a migration verb. **Nobody in Valoria can relocate** — `move` is TRAVEL (a `travel_leg` Tenure alter) and `residence` is a contested claim predicate **with no writer** | a verb row + an effect | a person's `residence` differs across two seasons in one run |
| **24a** | **6a — AFFILIATIONS** | IN | the affiliation roster + the incompatibility relation, as a table | `references/descriptor_registry.yaml` + `engine/season/rosters.yaml` | the roster loads and a person holds two incompatible affiliations at full intensity |
| **24b** | **6c — THE THIRTEEN** | IN | re-author the thirteen and their projection onto `memory · substantive · equity · selfish` | `rosters.yaml: tables.conviction_projection`, `tables.alignment` | `_load_projection`/`_load_alignment` raise at module scope, so both must exist before first import — the import IS the falsifier |
| **24c** | **6b — THE RENAME** | IN | rename the moral-value basis, which `STR-6` forces by reserving `conviction` | 29 Python files / **308 occurrences** under `engine/`, 51 YAML/JSON, **12** live `.md` | its falsifier already exists and is green |
| **24d** | **SE-CAPACITY** | SE | `capacity(w, rung)` as a Query over the rung's dwelling Sites **with a FLOOR — never a fixture table**; `found` (P4) is the throttle | `engine/season/queries/` — and **`dwelling` does not exist**: `rosters.yaml:847` fixes `site_kinds: [harbour, seam, body]`, three, one of which is not a site | **RULED, NOT GATED — see §6.** The blocker is that the ruled mechanism has ZERO code, not that it needs a decision |
| **P5a** | **ITEM 13** | IN | **unblocked** — `RR-A` → FOLD. It leaves Phase 5 and needs no ruling | per `01_THE_BUILD_ORDER.md` | — |
| **P5b** | **ITEM 15** | IN | `Act.via` + F3 — **still blocked** on ratified positions 3–5. The Arc-2 gate itself | — | not startable; listed so it is not re-derived as available |

**Ordering note.** `13c` before `19c` because `H-71` is Tier 0 and nine verbs are unreachable behind it;
`24a`/`24b` before `24c` because the rename is the expensive arm and the content must exist to rename
*to*; `24d` after `24a`–`24c` because it is the only row waiting on a person.

## §3 · THE ONE COST THIS AMENDMENT RE-PRICES, AND THE STALE FIGURE IT CORRECTS

⚠ **`01_THE_BUILD_ORDER.md:1028` says of 6b: *"`references/names_index.yaml` is the TERMS owner; the
rename derives."* BOTH HALVES ARE FALSE, MEASURED.**

1. **The executor is retired.** `names_index.yaml:13-14` advertises `tools/valoria_rename.py`;
   `references/restructure_ledger.md:1525` is that tool's `FORK:1e4c6f4` row. **The tool that would
   derive the rename was deleted.**
2. **`names_index.yaml` does not own the thirteen.** Its `conv.*` block is **seven** entries at
   `:105-111`, all `enforce: warn`, glossed as the 7-axis character conviction class. The real chain is
   `descriptor_registry.yaml:236` (`count: 13`) → `rosters.yaml:228` (`from_descriptor:`) →
   `descriptors.json`, behind the blocking `--check`.
3. **The 107-document arm has fallen to 12.** `adjudication_register.yaml:681` measured 107 *before*
   `ED-IN-0231`. `systems/` now holds **zero** `.md`; the live count is **12**, with 66 quarantined.
   `01_THE_BUILD_ORDER.md:1028` and `RULINGS.yaml:1356-1357` both carry the stale figure forward —
   `CLAUDE.md` §0.1 pt 3 row four, **inflating 6b nine-fold on its largest arm.**

**Net:** `6a` and `6c` are cheap and DO derive — Jordan's content, then one owner edit, with no
`engine/season/*.py` change, because `decision/choose.py:358-360` resolves the tables by name. **`6b`
does not derive and is a hand sweep** unless `valoria_rename.py` is restored from its fork ref first.
**That restore-or-sweep call is the one decision this file surfaces and does not take.**

## §4 · THREE COLLISIONS FOUND WHILE VERIFYING — recorded, not fixed

1. ⚠ **`R7` NAMES TWO LIVE RULINGS.** In `proposals/2026-09-16-conviction-decision-layer/` it is
   projection non-separability (`formal_analysis.md:183`); in Layer 2 it is the fan-out/witness ruling
   that took `fan_out_mode` off `total` (`engine/season/hole_register.yaml:2214`, `rosters.yaml:499`,
   `requirements.yaml:430`, `ED-IN-0205`). `2026-09-18-character-decision-layer/PROPOSAL.md` §1 cites
   bare `R7` as ratified without saying which. **`CLAUDE.md` §4's idempotence failure, exactly.**
2. **TWO `R3`s.** `PROPOSAL.md` §1's R3 is *"best design wins"*; `ED-IN-0251`'s R3 is *"the cells are
   yours."* R1 and R2 agree verbatim between them. **The ledger is the authority.**
3. **TWO LIVE BUILD ORDERS FOR ONE SUBSYSTEM, NEITHER CITING THE OTHER** —
   `01_THE_BUILD_ORDER.md` §7.5 and `PROPOSAL.md` §7. Dispositioned in `03_DECISIONS.md`; **not
   chosen.** Choosing is Jordan's or a later pass's, and picking one silently is how the corpus got
   two in the first place.

## §5 · ONE CORRECTION TO A FIGURE THIS SUITE'S OWN ORCHESTRATOR HANDED DOWN

⚠ **`R-08`'s *"tie breaks ALPHABETICALLY BY VERB"* IS NOT LIVE, and it was handed to a producer as
though it were.** `decision/choose.py:370` does sort `(-score, verb, subject)`, but **`:375` re-orders
through `_sample_order`**, which at the shipped `tau=0.1` samples via candidate-keyed Gumbel;
`:315-316` states outright that the trailing terms *"are not the tie-break — `g` is."*
`engine/season/requirements.yaml` corrects itself later in the same row (`:452`, `:472-474`), and the
head of that row was read without the correction. The `2–7 of 22` figure is likewise superseded by
`U3` to a **7.79 → 21.84** mean (`:393-401`).

**`R-08`'s live reason for `partial` is different and still true:** the tie is broken by the draw,
*"not a reason of theirs"* (`:462`). **This is the layered-`measured:`-block hazard for the third time
in one session** — `R-03` and `R-09` read the same way. **Read a `measured:` block to its end before
quoting its head.**


## §6 · ⚠⚠ `ED-SE-0051` IS RULED, AND FOUR SURFACES DISAGREE

**THIS FILE'S FIRST WRITING HAD `24d` GATED ON A RULING THAT ALREADY EXISTED, AND SO DID THIS SUITE'S
ORCHESTRATOR, TWICE, IN ITS REPORTS TO JORDAN.** Corrected here rather than quietly.

**The ruling, opened at the line:** `proposals/2026-09-17-governance-and-behaviour/RULINGS.yaml:1838-1844`
carries `disposition: ruled`, `ruled.by: "Jordan, 2026-09-17 (in session)"`, and the decision verbatim:

> **MATTER PLUS HEARTH CAPACITY. A `capacity(w, rung)` QUERY over the rung's dwelling Sites, with a
> FLOOR — never a fixture table. `found` (P4, "found and build") is the throttle. SCOPED TO
> POPULATIONS**, per the row's own discharge of `ED-WR-0011`'s pairing rider for NPC generation.

Its own `citation:` names `registers/editorial_ledger_se.jsonl:51`, so it is unambiguously this question.

**THE FOUR SURFACES:**

| surface | what it says |
|---|---|
| `RULINGS.yaml:1838-1844` | **RULED** — capacity arm, as a Query with a floor |
| `registers/editorial_ledger_se.jsonl:51` | `status: open`, `needs_jordan: true` |
| `registers/handoffs/HANDOFF_SE.md` | *"`ED-SE-0051` STAYS OPEN"* |
| both settlement suites | *"NOT RULED"* |

⚠ **AND `RULINGS.yaml` DISCLAIMS ITS OWN AUTHORITY** at `:5-6` and `:34-36` — *"NOTHING HERE RATIFIES
ANYTHING"*, and a `ruled` row *"is not a gate-step closure"*. **That disclaimer is about ratifying
DOCUMENTS, not about whether Jordan decided**; the file's own header defines `ruled` as *"the record of
what he decided"*. So the ruling is real and the ledger row is stale.

**THE FLAG IS DELIBERATELY NOT CLOSED HERE.** `CLAUDE.md` §0's step 1 — *"Superseded: a later ruling
decided it; cite the successor; close it"* — plainly applies, and the 2026-09-15 `SUPERSEDING ROW`
batch is the established precedent for how. **But closing a Jordan-gated row on a suite's own reading,
against three surfaces that say otherwise, is the kind of thing that wants his word** — the same
posture `ED-IN-0251` takes on `CURRENT.md:31`. **One `[editorial]` commit closes it whenever he says so.**

**WHAT IT COSTS EITHER WAY, MEASURED:** the ruled mechanism has **zero code** — no `capacity` in
`engine/season/queries/`, and **no `dwelling`, `houses` or `shelters` anywhere in `engine/season/`**.
`04_EVALUATION_part2.md:433` raised the missing site kind and was right. **The ledger row's own pricing
(*"matter-only costs nothing new; capacity costs one fixture table"*) is stale on BOTH halves** — the
ruling rejects the fixture table by name, and matter-only bites only in season 1 on the shipped corpus
(surplus grows: grain 2831, salt 2137 after two seasons) until P2 makes the population grow.
