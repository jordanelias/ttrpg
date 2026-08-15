# Character Stats, Faction Stats, and Progression — measured from code

## Status: PROPOSED — DESIGN-ONLY, HELD FOR JORDAN. No constant changed, no default flipped, no golden re-recorded, no `.py` touched. Every number below was **produced by running the engine at HEAD**, not transcribed from an audit.

**Date:** 2026-08-15 · **Lane:** IN (cross-cutting) · **IDs:** none allocated (design-only)
**Bears on:** `OPT-AV-1` (attribute roster, Jordan-SKIPPED 2026-07-08, still open) · `repo_state_armature_v1` P5 · fork plan C4 · M1 juncture 6

> ### Revision note — this document was rewritten twice on its own day
> Draft 1 recommended a Burning-Wheel test-marking system sized against a July audit's prose.
> Three independent read-only critics and then Jordan killed it, on four separate grounds:
> **(a)** the audit is stale — *read code, not prose*; **(b)** its anti-farm rule was inert because
> combat resolves against a fixed `DECISIVE_OB = 3`; **(c)** test-marking is unacceptable unless
> automated; **(d)** dice are continuous now, so a reward can be **+0.1D**, which dissolves the
> pricing problem draft 1 was contorting around. Draft 1 also contained two fabricated quotations.
> This version is measured, not cited. §1 records what was run.

---

## §1 WHAT I RAN, AND WHAT IT SAID

All figures below are from `systems/combat/combat_engine_v1/workbench/balance.py` at HEAD
(`26609fe`), position-swapped, Wilson 95% CI, deterministic seeding — the harness's own method.

### 1.1 Attribute parity, re-measured (n=600, baseline str/agi/end 4, rest 3, arming/light)

| attribute | win% | 95% CI | marginal | July audit said |
|---|---|---|---|---|
| **cog** | 70.4 | 66.6–73.9 | **+20.4pp** | +20.4pp (unchanged) |
| **history** | 64.9 | 61.0–68.6 | **+14.9pp** | +19.4pp — **moved −4.5pp** |
| att | 62.0 | 58.0–65.8 | +12.0pp | +11.6pp |
| end | 60.2 | 56.2–64.0 | +10.2pp | +8.2pp |
| strength | 59.2 | 55.2–63.0 | +9.2pp | +11.4pp |
| agi | 56.3 | 52.2–60.2 | +6.3pp | +5.2pp |
| spirit | 56.0 | 52.0–59.9 | +6.0pp | +6.5pp |
| disp | 54.7 | 50.7–58.7 | +4.7pp | +5.4pp |
| **focus** | 50.3 | 46.3–54.3 | **+0.3pp** | −0.7pp |
| *mirror control* | *53.1* | *49.1–57.1* | — | — |

Jordan was right that the audit is stale — but only partly, and it matters which part. **`cog` is
identical; `history` has moved by 4.5pp.** So the audit's *ranking* survives and its *values* do not.
The conclusion the ranking forces is unchanged and is the governing constraint of this document:

> **A whole attribute point is worth 6–20pp. The mirror control's own CI is ±4pp. There is no
> integer-attribute progression system that is not a balance event.**

And one row is a finding in itself: **Focus is worth +0.3pp** — indistinguishable from zero, at a
mirror control that itself reads 53.1. Focus is also *declared but never read* in threadwork
(`operations.py:16` names it in the docstring; no function body touches it). It is the one attribute
the engines demonstrably do not use.

### 1.2 The continuous-dice probe — Jordan's +0.1D, measured

Two lines quantize the pool, and both are wrappers around a primitive that is already continuous
(`dice_engine.continuous_engine_sample`: *"Pool may be fractional"*):

- `engine/autoload/sigma_leverage.py:265` — `roll_net`: `effective_pool = max(1, int(round(pool)))`
- `engine/autoload/sigma_leverage.py:277` — `roll_net_continuous`: same
- `systems/combat/combat_engine_v1/core.py:52` — `resolution_pool`: `int(round(history)) + BASE_POOL`

Removing `resolution_pool`'s rounding **alone** gives a broken curve — flat at +0.1/+0.2/+0.3, then a
jump at +0.5. That discontinuity is `roll_net` still rounding underneath. Removing **both**
(measurement-only monkeypatch, n=1200):

| History increment | win% | 95% CI | marginal |
|---|---|---|---|
| *mirror control* | *49.58* | *46.7–52.4* | — |
| **+0.10D** | 53.01 | 50.2–55.8 | **+3.0pp** |
| +0.25D | 52.32 | 49.5–55.1 | +2.3pp |
| +0.50D | 57.58 | 54.7–60.4 | +7.6pp |
| +1.00D | 65.97 | 63.2–68.6 | +16.0pp |

The curve is smooth and the 0.5D discontinuity is gone. **+0.1D is ~+1.6pp on a linear read, and
+0.10D/+0.25D are not separable at this n** — i.e. it sits at or under the noise floor. That is
exactly the property a progression quantum needs, and it is why *"round to .1, never integers"* is
the enabling ruling for everything in §4.

### 1.3 What the engines consume — the bottom-up census

**The engines never consume a bare attribute. They consume blends.** Every attribute reference in
`combat_systems.py` is inside a weighted sum the engine computes as a *faculty*:

| Faculty the engine computes | Formula, from code | Site |
|---|---|---|
| **Reading** | `(2·Cog + Att)/3 + K·(History−3)` | `combat_systems.py:171` |
| **Reflex** | `(w₁·Agi + w₂·Att) / Σw` | `:172` |
| **Balance** | `½Agi + ½Str − 1 + skill('balance')`, × fatigue × poise | `:188` |
| **Tempo** | `BASE + K·(Agi−4) − pen` | `:113` |
| **Impact** | `Strength + heft` | `core.py:537` |
| **Durability** | `WI = End + 4 + 0.4·Spirit`; `Health = WI·(MW+1) + 0.25·Str·End` | `combatant.py:20-47` |
| **Concentration** | `3·Focus + 2·Spirit`; `poise_regen`, `disrupt_resist` off Focus | `:1435`, `:1451` |
| **Thread pool** | `2·Spirit + History + TPS` | `threadwork/sim/operations.py:151` |
| **Command** | `⌈(2·Cha + Cog)/3⌉` | mass battle |

Three attributes fall outside this entirely, and the way each falls out is different:

| Attribute | Engine presence | What it actually is |
|---|---|---|
| **Bonds** | Only as a **gate** — `bonds_a < KNOT_BONDS_MIN` (≥5), count `floor(Bonds/2)+1` (`knots.py:185`). Never in a pool. | a **capacity**, not a faculty |
| **Recall** | **Zero.** Every `Recall` hit in `.py` is mass battle's `recall_check` — pulling back a pursuing unit, an unrelated homonym. | a **capacity** (equip slots, learning rate) — and entirely unbuilt |
| **Charisma** | **Zero occurrences in any `.py` file in the repository.** | unbuilt; its only specified roles are Command and `Face_max` display |

### 1.4 The answer to "are attributes tacked on?"

**Yes — and the code says so in a specific, diagnosable way.** The 3/3/3+1 spread is a *character-sheet
taxonomy* (body / mind / social / metaphysical). The engines group by something else entirely — by
**which reservoir or which channel** an input feeds:

| Emergent grouping the code uses | Members | Cuts across body/mind/social? |
|---|---|---|
| Mechanical | {Strength, Agility} | no |
| Reservoir | {Endurance, Spirit} | **yes** — body + metaphysical |
| Perception | {Cognition, Attunement} | **yes** — mind + social |
| Attention | {Focus, Spirit} | **yes** — mind + metaphysical |
| Command | {Charisma, Cognition} | **yes** — social + mind |

Every grouping the engines actually compute except one **cuts across the imposed partition.**
Spirit appears in three of the five. That is the signature of a taxonomy imposed on top of a system
that wanted a different one — which is precisely the "tacked on" intuition, now with a citation.

**So the bottom-up roster the systems suggest is two-tier, not 3/3/3+1:**

- **Tier 1 — Faculties** (blend into resolution): Strength · Agility · Endurance · Cognition ·
  Attunement · Spirit. Six, all measurably load-bearing (+6.0 to +20.4pp).
- **Tier 2 — Capacities** (gate what you may hold, never roll): Recall (skills held, learning rate) ·
  Bonds (Knots held). Two, structurally different from Tier 1 and correctly so.
- **Contested:** Focus (+0.3pp, unread in threadwork) and Charisma (zero code) — the two the
  evidence cannot presently justify as either.

---

## §2 THE ROLE QUESTION

*"I don't see the best way to have a character being good as a spy or detective or interrogator, a
combatant, general, debater, politician, orator, governor, leader."*

The ten split into **six skill roles and four position roles**, and they need different machinery.

| Role | Kind | Carried by | Built? |
|---|---|---|---|
| Combatant | skill | History pool + weapon + tradition + techniques | **fully** |
| Debater / Orator | skill | `faculty` + Standing/ethos + Room/pathos + Dossier + style | kernel built, **no attributes** |
| Detective | skill | Examine/Research/Reconstruct + Evidence Track | prose only — sim is `stub_resolve` |
| Spy | skill | Cover + Concealment + Exposure + Shadow Renown | prose only |
| Interrogator | skill | Dialogue Lattice + Disposition leverage | prose only |
| **General** | **position** | Command `⌈(2Cha+Cog)/3⌉` + unit quality — **and an army** | partly |
| **Politician** | **position** | Standing ladder + Mandate/votes — **and a seat** | prose only |
| **Governor** | **position** | AP × compliance + Ledger — **and a settlement** | partly built (`registry.py`, `ledger.py`) |
| **Leader** | **position** | Standing 7 / faction emergence — **and a faction** | prose only |

Two consequences fall straight out:

**(1) Attributes cannot distinguish these roles, and were never going to.** The same Cognition is
primary for detective, spy *and* general. The same Charisma is primary for orator, politician *and*
general. A 10-attribute spread has less differentiating power across these ten roles than a
3-attribute one would, because the roles are not distinguished by *aptitude* — they are distinguished
by **practice, instruments, and office**.

**(2) The one role Valoria expresses well uses no attribute in its pool.** Combat is
`max(5, History + 6)` — attribute-independent by ratified design (ED-901). Identity there comes from
**weapon morphology (up to +47pp), armour (+46pp), tradition as a channel-reweighting profile, and
graded techniques (~0pp aggregate, ~12–13% per-fight texture)**. That is a *working* role architecture,
and it works because identity lives in **kit and school**, not in a stat spread.

### 2.1 The generalisation

The combat stack, abstracted, is the answer to the role question:

| Layer | Combat instance | Detective | Spy | Debater | General | Governor |
|---|---|---|---|---|---|---|
| **Pool** — how practised | History | investigative practice | tradecraft practice | forensic practice | command practice | administrative practice |
| **Instruments** — what you bring | weapon, armour | archive access, lattice | cover identity, network | **Dossier / EvidenceItem** *(already built)* | formation, tactic cards | **Ledger, AP** *(already built)* |
| **School** — channel reweighting | tradition | method | tradecraft school | style (Memory/Projection × Revealing/Obscuring) *(built)* | doctrine | governing ethos |
| **Techniques** — graded levers | `equipped` *(built)* | — | — | — | — | — |
| **Temperament** | disposition | — | — | — | — | — |
| **Faculties** — modulate, don't select | Str/Agi/End/Cog/Att/Spi | ditto | ditto | ditto | ditto | ditto |
| **Office** — *position roles only* | — | — | — | — | **an army** | **a settlement** |

Three of those cells are already built outside combat and are not currently thought of as the same
thing: the contest kernel's `Dossier`/`EvidenceItem`, its four-way style axis, and settlements'
`ledger.py` + `registry.ap`. **The architecture exists in three places and has never been named
once.** Naming it is most of the work.

---

## §3 THE ATTRIBUTE PROPOSAL

Bottom-up (§1.3–1.4), presented as alternatives so OPT-AV-1 can be ruled rather than authored.

| | Option | Roster | Verdict |
|---|---|---|---|
| **A-1** | **Six faculties + two capacities** | Str · Agi · End · Cog · Att · Spi ‖ Recall · Bonds | **RECOMMENDED** — what the code actually computes |
| **A-2** | Ratify the 10 unchanged | + Focus, Charisma | Zero migration; keeps two attributes with no measurable effect |
| **A-3** | A-1 but re-home Focus rather than cut it | Focus → a *derived* Concentration term | The compromise, if cutting is too strong |
| **A-4** | The registry's 9 (drop Recall) | — | **REJECT** — deletes the skill-capacity spine with no replacement home |
| **A-5** | The glossary's 7 | — | **REJECT** — stale table; deletes Focus, Bonds *and* Recall |

**A-1 in detail.** Two tiers, because the code has two tiers:

- **Faculties (roll):** Strength · Agility · Endurance · Cognition · Attunement · Spirit.
  All six measured at +6.0 to +20.4pp. They enter resolution only through the blends in §1.3 —
  the character sheet may still present them, but no system reads a bare one.
- **Capacities (gate, never roll):** **Recall** — how many Histories you may hold active and how fast
  you learn; **Bonds** — how many Knots you may hold. Neither appears in any pool, in canon or in code.
  Making that distinction explicit is the fix for Recall's current triple-gate (breadth + depth +
  learning rate), which makes it a mandatory tax stat: **capacities govern breadth, never depth.**

**On Focus.** Measured +0.3pp; unread in threadwork despite being declared; its stated canonical job
(Thread ops per contact session) is unimplemented. Three honest options, and I do not think the
evidence picks between them: cut it (A-1), keep it as a derived term inside Concentration (A-3), or
keep it and *give it a job* — the obvious one being that it should govern the **Attention** faculty
that `poise_regen` and `disrupt_resist_p` already reach for. **This is a Jordan call, not a
measurement call.**

**On Charisma.** Zero code. Its two specified jobs are Command (`⌈(2Cha+Cog)/3⌉`) and `Face_max`
display. If the social layer is going to carry four of the ten roles, Charisma probably has to
survive — but it has to be *given* a resolution role, not assumed to have one.

---

## §4 PROGRESSION ON CONTINUOUS DICE

### 4.0 The enabling ruling

*"We need continuous. We can round to .1 but never do integers for dice."* Everything below depends
on it, and §1.2 measures why: **at +0.1D granularity a reward is ~+1.6pp — an order of magnitude
below a whole attribute point, and at or under the noise floor.** Integer dice make every reward a
balance event; tenths make progression tunable for the first time.

**Precondition (small, three lines):** de-quantize `sigma_leverage.roll_net` and `roll_net_continuous`
(`:265`, `:277`) and `core.resolution_pool` (`:52`). The primitive underneath already accepts
fractional pools. ⚠️ This is a **behaviour change**, not a repair — it moves every seeded trajectory
and will re-record goldens. It needs its own gated increment, an expected-delta test, and a golden
regen; it must not ride in on a design PR (`CLAUDE.md` §0.1).

### 4.1 The shape

**Progression is access and instruments, not numbers.** Three ladders, in descending safety:

| Ladder | Grain | Measured cost | Automatable? |
|---|---|---|---|
| **Instruments & techniques** | discrete unlocks | **~0pp aggregate, 12–13% per-fight texture** | yes — unlock on use/instruction |
| **Practice** (the History layer) | **+0.1D increments** | **~+1.6pp each** | yes — accrues from the resolution record |
| **Faculties** (attributes) | whole points | **+6 to +20pp** | should be **rare and authored**, not earned |

The first is where most of the felt progression should live, because it is the only channel *measured*
to sit inside the noise floor while still changing how fights play out. The second is the dial. The
third should barely move.

### 4.2 Practice, automated

Jordan's constraint — *no Burning Wheel unless automated* — is satisfiable, because the award falls
out of data the resolver already emits. **No player bookkeeping, no marks to track, no GM:**

- Every resolved action already produces `(pool, Ob, degree)`. On resolution, the engine adds a small
  increment to the Practice that was used. `[SEED]` shape: **+0.02D on a decided action, +0.05D when
  the action was *contested and lost*** — failing against real opposition teaches more than winning
  against none. Ten to twenty engagements → +0.1 to +0.5D. The player sees a bar, never a ledger.
- **Anti-farm must key on opposition, not on Ob.** Draft 1 keyed it on Ob and that was inert: combat
  resolves against a **fixed `DECISIVE_OB = 3`** (`core.py:45`, `:104`) and carries the opposition in
  `net_sigma`. The quantity that varies *is* `net_sigma`. Scale the increment by the opposition faced
  — which also makes it self-flattening, since a practised character faces relatively weaker
  opposition for the same absolute challenge.
- **Fidelity-invariance is then free**: auto-resolved seasons emit the same tuple, so a player who
  zooms out is not punished. This was draft 1's argument for test-marking and it survives the
  mechanism's death, because it was never about marking — it was about awarding off the *record*.

### 4.3 What does not move
Faculty points should be **authored, not earned** — granted at named story moments (Conviction
resolution, a Lineage Act, a Rendering Crisis survived), capped hard, and priced against §1.1's
table rather than against a season count. Draft 1 tied them to Conviction resolution and sized the
budget at 2–6; that was **wrong** — Portrait Retirement's 2-of-3 is an *unlock*, not a cap, and new
Convictions are written on fulfilment, so the real ceiling was 10–15 points. At +6 to +20pp each,
**the defensible budget may well be zero**, with the instrument and Practice ladders carrying the
whole arc. That is a better fit to Portrait Retirement's "a chapter of a life" thesis anyway.

---

## §5 FACTION STATS — CORRECTED

| | Option | Verdict |
|---|---|---|
| F-1 | Ratify canon as-is (W · Mil · I · Sta · Intel + derived Mandate) | safe; keeps a dead stat |
| F-2 | **Cut the Intel scalar; re-home it as an Intelligence Holdings ledger** | **RECOMMENDED** |
| F-3 | Split derived Mandate into **Mandate** (elite/settlement Legitimacy) and **Support** (popular) | **RECOMMENDED** |
| F-4 | ~~New `Administration` stat~~ | **WITHDRAWN** |

**F-2.** Intel is declared 0–7 and is *"currently unread/unwritten by live code"* (`game_state.py`).
Its real gameplay is *knowing specific things about specific parties* — a ledger, which
`derived_stats_v30` §14.1 already lists as **Intelligence Holdings (PENDING)**, and which composes
directly onto the single-owner `systems/settlements/sim/ledger.py`, whose five tag kinds already
include **Leverage** (*"a hook the player holds"*). Leverage *is* intelligence.

**F-3.** Settlement scale correctly separates Legitimacy from Popular Support (0–7 each, LPS-2e);
faction scale collapses both into one Mandate. Parliament should count Mandate; Muster, Turmoil and
Revolt should read Support. Without the split, "beloved locally, distrusted at court" is
mechanically inexpressible — and that is most of this setting's politics.

**F-4 withdrawn, and why it is worth recording.** Draft 1 proposed an `Administration` stat plus a
derived `Chancery`, on the reasoning that administrative reach was unmodelled. It is modelled:
`registry.py:92` defines `Settlement.ap`, and `lps_wiring_v1.md:95` specifies
`floor(s.ap * compliance(s))` — self-described as *"the CK3-Administrative shape realized as a
formula."* Draft 1 cited Clerk Capacity (which that same doc defines as an **AP source**) and then
lifted a per-settlement quantity into a flat faction scalar — replacing an emergent aggregate with a
top-level number, the anti-emergence direction. The correct move is the opposite: **aggregate `ap ×
compliance` upward** to give factions administrative reach, and name nothing new.

**Also withdrawn:** renaming faction Discipline → *Cohesion*. `Cohesion` is the name **PP-232
retired** (`mass_battle_v30.md:7`, `glossary.md:153`), so the rename fails the very
idempotent-in-meaning rule (`CLAUDE.md` §4) it was invoked to satisfy.

---

## §6 CORRECTIONS AND WITHDRAWALS FROM DRAFT 1

Recorded because a proposal that quietly drops its errors teaches nothing.

| # | Draft-1 claim | Status |
|---|---|---|
| 1 | Craft clock keyed on `Ob ≥ level+1` | **WITHDRAWN** — combat's Ob is fixed at `DECISIVE_OB = 3`; the invariant was inert where measurable. Replaced by an opposition-keyed increment (§4.2). |
| 2 | Attribute points from Conviction resolution, budget 2–6 | **WITHDRAWN** — real ceiling 10–15; at +6 to +20pp/point the defensible budget may be zero. |
| 3 | New faction `Administration` stat | **WITHDRAWN** — `ap × compliance` already exists. |
| 4 | Faction Discipline → *Cohesion* | **WITHDRAWN** — resurrects a PP-232-retired name. |
| 5 | P7's "no-exchange rule" between clocks | **REFUTED, not untestable** — Standing buys scene actions (+1 at 4–5, +2 at 6–7, +1 per local Knot, `player_agency_v30` §6.2), and scene actions are the input to every clock. |
| 6 | Renown decay −1/idle season at ≥5 | **SOFTENED to a question** — the premise was false (Renown already has a downward arm via governance penalties) and it would break the faction-emergence latch, where Renown 5/7/9 are gates and a founded faction's Influence is *seeded* at `floor(Renown ÷ 2)`. |
| 7 | `UPSET_FLOOR` "self-labelled non-emergent designer fiat" | **FABRICATED QUOTE, REMOVED.** Actual text: `[DESIGNER RULE — Jordan; deliberate, NOT an emergent mechanic]`, which exists to *distinguish itself from* ungrounded fiat. It does carry a real measurement consequence: every reported win-rate is compressed toward `[0.05, 0.95]`. |
| 8 | A "Jordan quote" on investment-vs-membership | **MIS-ATTRIBUTED, REMOVED** — a compression of two numbered principles in a doc bylined *PC-lane audit node*. The principle is real; the attribution was not. |
| 9 | D3's "binding rule" quote | **RE-ATTRIBUTED** — it is from the curriculum proposal's *reading* of D3, not from the balance report. |
| 10 | Ability layer "16–28% texture / 3–8% flip" | **CORRECTED** (caught in draft 1's own pass) — 16–28% is retracted in the test's docstring (ED-PC-0034); true rate ~12–13% at n=200; the flip figure had no source. |
| 11 | §1.3's grep-count "measurement" of attribute load | **REPLACED** — it *inverted* the true ranking (Strength grep-15 → +9.2pp; Cognition grep-2 → +20.4pp). §1.1 now uses the real harness. |

---

## §7 DEFECTS WORTH FIXING WHATEVER IS RULED

Each is independent of every design call above.

1. **Threadwork History is inert.** `history_contrib = min(3, history + 3)` — `_actor_pool` returns
   **12 for history 0, 3 and 7 alike** (run 2026-08-15; `history = −2` returns 10). ⚠️ Fixing it is a
   **behaviour change**, not a repair: the PP-624 comment implies the intent was `min(3, history) + 3`
   (range 3→6), which at history 3 is +3D ≈ +1.2 expected net, and there is **no oracle for
   threadwork**. Gate it.
2. **`sim/conviction.py` runs a superseded 9-Conviction set** while canon is 13, and a live caller
   passes `'Loyalty'` — a member of neither — which silently no-ops.
3. **Standing has at least four live ranges**: 0–5 (`clock_registry_v30`), 0–7 (`faction_politics_v30`,
   which explicitly supersedes 0–5), both inside `player_agency_v30`, and **0–10 in the live contest
   kernel** (`primitives.py:121`, feeding `Face_current`). A blind sweep to 0–7 would change kernel
   behaviour — this is not a currency correction.
4. **`clock_registry_v30` has no Renown row at all**, though Renown is stated 0–10 at
   `player_agency_v30:406` — so OPT-AV-18's "cap" half is already answered in canon.
5. **`valoria_ttrpg_complete.md §10.2`, cited as the CP spending menu, has never existed in this
   repository** — checked across all commits on all refs, with a positive control.

---

## §8 THE CALLS THAT ARE JORDAN'S

1. **OPT-AV-1 — the roster.** Recommended **A-1**: six faculties + two capacities, derived from what
   the engines compute rather than from body/mind/social. The live alternatives are A-2 (ratify 10
   unchanged) and A-3 (keep Focus as a derived term).
2. **Focus** — cut, re-home, or give it a job. Measured +0.3pp, unread in threadwork. No measurement
   picks between the three; this is a design call.
3. **Charisma** — zero code. If the social layer carries four of the ten roles it probably must
   survive, but it needs a resolution role rather than an assumed one.
4. **De-quantizing the dice** (§4.0). Three lines, but a behaviour change with a golden re-record.
   Worth scheduling as its own gated increment; everything in §4 waits on it.
5. **Whether faculty points move at all** (§4.3). The measured answer may be "no", with instruments
   and Practice carrying the arc.
6. **F-2 / F-3** — the Intel re-home and the Mandate/Support split.
7. **Aging.** Absent corpus-wide. Raised, not answered.

---

## §9 WHAT WOULD FALSIFY THIS

- **F-A — "+0.1D is inside the noise floor."** Re-run §1.2's probe at n ≥ 3000. If +0.10D separates
  from the mirror control by more than the CI, the quantum is too large and must drop to +0.05D.
- **F-B — "instruments are safe to grant generously."** `test_levers_add_texture_without_shifting_balance`
  guards divergence ≥5% and flips ≤20%; re-run with a deep `equipped` kit. Note the two known
  exceptions at *maximum* investment (`shinogi L8` at 56.4; a deep dagger grappler at 24.3) — the
  ~0pp claim is an aggregate, not a promise at the tail.
- **F-C — "faculties should barely move."** Already answered by §1.1 and not open: +6 to +20pp per
  point against a ±4pp control. The open question is not whether, it is whether the budget is zero.
- **F-D — "Practice increments are automatable with no GM."** Build the accrual against the resolver's
  emitted tuple and show a seeded campaign producing a Practice curve with no human adjudication.
  Not yet run.
- **F-E — the role architecture (§2.1) is unfalsifiable today**, because four of the six skill roles
  have no resolver. Stated as an assumption, not a result.

---

*End proposal. PROPOSED — design-only, held for Jordan. Nothing ratified.*
