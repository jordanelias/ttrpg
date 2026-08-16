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

---

## §10 THE CODE-DERIVED ATTRIBUTE CENSUS (added on Jordan's direction: read the code, no grep)

### 10.1 What every resolver actually asks of an actor

Read from the resolvers themselves, not matched by token.

**Combat.** No attribute reaches resolution directly. Every one enters through a *faculty function*:

| Faculty (computed per beat) | Governing inputs | Modulated by | Site |
|---|---|---|---|
| Impact | Strength + weapon heft | — | `core.py:537` |
| Handling deficit | Strength vs `str_demand`(weapon) | fatigue | `combat_systems.py:179` |
| Tempo | Agility `+K·(agi−4)`, weapon | fatigue, poise | `:113` |
| Balance | ½Agi + ½Str + `skill('balance')` | poise, fatigue | `:188` |
| Reading | (2·Cog + Att)/3 + K·(History−3) | — | `:171` |
| Reflex | (w₁·Agi + w₂·Att)/Σw | — | `:172` |
| Durability | WI = End+4+0.4·Spirit; Health = WI(MW+1)+0.25·Str·End | wounds | `combatant.py:20-47` |
| Action economy | `stamina_max` = 3·End + 2·Spirit | `act_cost`(heft, commit) | `:27` |
| Steadiness | `conc_max` = 3·Foc+2·Spi; `disrupt_resist`; `poise_regen` | — | `:1435`, `:1451` |
| **Pool** | **`max(5, History + 6)` — no attribute** | — | `core.py:50` |
| Aggression | `disp_lean` = (disp−4)/3 | — | `:186` |

`balance_eff` carries a ruling in its own comment that generalises: **"BALANCE is NOT a stat (Jordan):
it is GOVERNED BY AGILITY, modulated by CURRENT poise."** That is the architecture — *attributes
govern, faculties resolve, state modulates* — and it is already law in the one finished engine.

**Contest kernel.** Refuses attributes outright. Its primitives are Standing/Face (0–10, ethos-built),
Room (pathos), Reserve (stamina, MAX 12), Stasis (6-rung ground), Readiness = Standing.frac ×
Room.frac, Resonance/leak, Dossier/EvidenceItem, and `faculty`. Charisma exists only as a derived
*view* (`FaceScale.face_max = Cha × 3`), explicitly *"not kernel state."*

**Threadwork.** Spirit (pool ×2), TS (gate + TPS), Cognition (collective helper only), History (inert).
**Knots.** Bonds (gate ≥5; count `floor(B/2)+1`), Spirit, History(Relationships), TS, Disposition.
**Mass battle.** Command = `⌈(2·Cha + Cog)/3⌉`; otherwise unit stats.

### 10.2 `faculty` is the Primary-Attribute slot, made per-domain

`primitives.py:208-211` — `class Pool: BASE = 3; size(faculty) = max(5, faculty*2 + BASE)`.

That is the canonical Universal Pool `(Primary × 2) + History + 3, min 5` with History folded to 0.
The kernel did not invent a primitive: it took the canonical formula, declined to commit to *which*
attribute fills the Primary slot, and abstracted the slot. Every pool in the game is then one shape:

| System | aptitude slot | practice slot | base |
|---|---|---|---|
| Universal (canon) | Primary × 2 | + History | + 3 |
| Contest kernel | **`faculty` × 2** | — | + 3 |
| Combat | **removed (ED-901)** | + History | + 6 |
| Threadwork | Spirit × 2 | + History *(inert)* + TPS | — |
| Fieldwork | Primary × 2 | + History | + 3 |

**Proposal: make `faculty` the single owner of the aptitude slot, DERIVED and PER-DOMAIN.**
`faculty(domain) = f(governing aptitudes, practice in that domain)`.

Why this is the right answer to *"what attributes are appropriate, primary or derived":*

1. **It is per-domain, so it cannot become a "who-bought-X" contest.** That degeneracy is not
   hypothetical — `traditions.py`'s header records it: *"The scalar 7-channel weight vector was
   REMOVED 2026-06-29 (Jordan) — proven a degenerate 'who-bought-balance' contest."* A single global
   aptitude scalar has exactly that shape. A vector of per-domain faculties does not, because
   investment in one is not investment in another.
2. **It preserves ED-901 rather than fighting it.** Combat's ruled position — pool is practice, not
   aptitude — is just `faculty(arms)` weighted heavily toward practice. No supersession needed.
3. **It is what "distinctive" actually means.** *Good as a spy vs a debater vs a combatant* is a
   statement about a **faculty vector across domains**, not about a Cognition score. Ten global
   attributes cannot express it; a faculty per domain expresses nothing else.
4. **It collapses five bespoke pool formulas to one owner** (`CLAUDE.md` §8, every rule lives once).

### 10.3 Classification of the current ten

| Attribute | Verdict from code | Evidence |
|---|---|---|
| **Strength** | **PRIMARY** — irreducible; Impact, handling, bind, grab, Health buffer | +9.2pp |
| **Agility** | **PRIMARY** — irreducible; tempo, footwork | +6.3pp |
| **Endurance** | **PRIMARY** — irreducible; WI, Health, stamina | +10.2pp |
| **Cognition** | **PRIMARY** — reading (2/3), collective thread, Command | **+20.4pp** |
| **Spirit** | **PRIMARY** — thread pool/threshold; low-weight in WI/Health/stamina/conc | +6.0pp |
| **Attunement** | **WEAK PRIMARY** — never appears alone; a 1/3 term in reading, a minority term in reflex | +12.0pp |
| **Focus** | **CONTESTED** — governs only `conc_max`/`disrupt_resist`/`poise_regen`; declared-but-unread in threadwork | **+0.3pp** |
| **Charisma** | **CONTESTED** — zero occurrences in any `.py`; specified only in Command and a derived Face view | unmeasurable |
| **Recall** | **CAPACITY, not attribute** — equip slots + learning rate; never rolled; zero engine presence | — |
| **Bonds** | **CAPACITY, not attribute** — Knot gate and count; never rolled | — |

**Candidates the code computes that are NOT attributes and should stay derived:** Balance (ruled),
Reflex, Reading, Tempo, Impact, Durability, Steadiness, Command.

**Candidates the code reaches for that no attribute supplies — and where distinctiveness actually
lives today:** `skill(axis)` on six named axes (bind · parry · dodge · balance · technique · grab),
`equipped` graded technique investment, `known_traditions` cross-training, `familiarity` (how well
you read a style you have met), Disposition, and Thread Sensitivity. Six inputs, one of which
(Disposition) appears on the character sheet. **That is the mechanical-distinctiveness surface, and
it is almost entirely invisible to the attribute roster.**

### 10.4 The distinctiveness answer, stated plainly

An attribute is a monotone scalar: more is always better, it moves aggregate win-rate (§1.1: 6–20pp),
and it produces **no texture** — the character does not play differently, they win more often. That is
the D3 monotone-stat failure, and it is why both finished engines removed attributes from their pools
independently (ED-901 in combat; `faculty` left unbound in contest).

What produces texture is measured and is already in the tree: **graded technique investment** (~0pp
aggregate, ~12–13% of fights play out differently) and **kit** (weapon spread up to +47pp with
deliberately spiky matchup tables under the ratified "no option globally best" principle). Jordan has
already ruled twice in this direction — the tradition weight-vector removal, and `IMPOSITION_GATE`'s
retirement in favour of *"efficacy EMERGES from the invested level, not tradition membership."*

**⚠️ Correction (Jordan, same session): for combat specifically, that is already DONE.** Abilities-as-
primitives, tradition-as-a-bundle-of-abilities, the imposition gate retired, *"efficacy EMERGES from
the invested level, not tradition membership"* — all shipped. So the paragraph above is not a
proposal; it is a description of `systems/combat/`. Restating it as a recommendation is the same
sampling error as §1.3's grep census: **generalising from the one subsystem that has an engine.**

### 10.5 The finding that survives once combat is excluded

Combat is the only system that has an acquisition layer. Ask what each *other* system has in the
same slot:

| System | Pool aptitude | Acquisition layer (the kit/school/technique tier) | Status |
|---|---|---|---|
| **Combat** | removed (ED-901) | weapons · traditions · `equipped` graded abilities · `skill()` on 6 axes · familiarity | **DONE** |
| Governance | AP × compliance | **Ledger tags** — Precedent · Grudge · Debt · Reputation · Leverage, durable, survive succession | **partly built** |
| Social contest | `faculty` (abstract) | style (2×2) is a per-contest *choice*; Dossier is evidence. **No learned-technique tier at all.** | **absent** |
| Threadwork | Spirit ×2 + TPS | operations are typed by scale; no school, no kit, no invested technique | **absent** |
| Mass battle | Command (2Cha+Cog)/3 | tactic cards — `FACTION_TACTIC_CARD_POOL_MODIFIERS = {}`, an empty stub | **absent** |
| Fieldwork | Primary ×2 | none (sim is `stub_resolve` throughout) | **absent** |

**Four of six systems have no acquisition layer, and those four are exactly the four that still lean
on attributes as their primary differentiator.** That is not a coincidence and it reframes the whole
roster question:

> **An attribute dependency is what a subsystem has instead of an acquisition layer.** Combat had
> `(Agility×2)+History+3` until it grew weapons, traditions and abilities — then ED-901 removed the
> attribute. Contest never committed to one, and abstracted the slot to `faculty`. Fieldwork's seven
> attribute-primaries are a placeholder for the tradecraft/method tier it does not yet have.

So the honest prediction is that **the attribute roster shrinks as the other systems get built**, and
sizing it now against subsystems that will change is premature for exactly the ones it looks most
needed for. What will *not* be replaced by an acquisition layer, because no amount of training
substitutes for it, is the substrate tier: **Strength · Agility · Endurance** (bodily) and
**Spirit / Thread Sensitivity** (substrate contact). Those are the durable primaries. Cognition,
Attunement, Focus, Charisma, Recall and Bonds are all doing work that a built subsystem would plausibly
re-home into method, evidence, standing, reputation, or capacity — and two of them (Charisma, Recall)
have no engine presence to defend today.

**The actionable consequence:** the highest-value next move for mechanical distinctiveness is **not**
ruling the roster. It is building the acquisition tier for one non-combat system — the contest kernel
is the ready candidate, since it already has Standing, Room, Dossier and Stasis and lacks only the
learned-technique tier — and seeing which attributes it still needs afterwards. That is the same
sequence combat ran, and it ended with an attribute being removed rather than chosen.

---

## §11 THE NO-ROUNDING RULING — COMPLETE SITE CENSUS

**Jordan, 2026-08-15: "I do not want any fractional dice pools or obstacles to be rounded or treated
only as integers."** This is not a new ruling. It is **ED-IN-0187 (2026-08-14)**, and the tree
already documents, in two places, that it was recorded and never executed:

- `engine/autoload/dice_engine.py:118-123` — *"`ob` is RULED to become fractional (Jordan,
  2026-08-14: an obstacle rolled against a character or faction is 'their corresponding score/2 plus
  whatever specific modifiers exist for them in that instance') but ⚠ **THAT DERIVATION IS
  IMPLEMENTED NOWHERE** — every call site in the tree still passes a hand-set Ob."*
- `systems/factions/sim/faction_action.py:106-111` — *"⚠ **THE POOL IS STILL NOT FRACTIONAL**…
  Jordan ruled 'fractional dice'; only the fractional RESULT is implemented. ED-IN-0187 recorded this
  correction and it was written into the ledger without being applied here — which is worse than an
  unimplemented feature, because the call site asserted the opposite."*

Census by AST (every `int`/`round`/`floor`/`ceil`/`//` applied to a pool, obstacle, or aptitude term
across the eight live resolver trees). **22 sites.** Classified by what each one blocks:

### A — The die-roll boundary (blocks ALL fractional pools; fix these three and the rest become visible)
| Site | Code | Effect |
|---|---|---|
| `sigma_leverage.py:265` | `roll_net`: `max(1, int(round(pool)))` | quantizes every discrete-path pool |
| `sigma_leverage.py:276` | `roll_net_continuous`: same | quantizes the **continuous** path too — the one that must not |
| `core.py:52` | `resolution_pool`: `int(round(history)) + BASE_POOL` | quantizes combat's only pool input |

`dice_engine.continuous_engine_sample` underneath already documents *"Pool may be fractional"* and
samples `Normal(μ·pool, σ·√pool)` with no rounding. **The primitive is already correct; only the
wrappers are wrong.**

### B — Obstacles rounded (direct violations, live)
| Site | Code | Note |
|---|---|---|
| `tribunal.py:119` | `max(1.0, round(base_ob * TRIBUNAL_RESISTANCE_HALVED_FACTOR))` | `base_ob = float(accused.L)` — an Ob that is **already a float** is rounded to an integer |
| `tribunal.py:122` | `max(1.0, round(base_ob))` | same |

⚠ Both then log `f"Ob {base_ob:.1f} -> {effective_ob:.1f}"` — it **prints one decimal place while
having already rounded the fraction away.** That is the worst failure mode: it reads as fractional
and is not.

### C — Integer-only pool arithmetic (each independently truncates)
`massbattle.py:879, 880` `math.floor(a_pool_raw/b_pool_raw)` · `:945, 946` `a_pool // 3`, `b_pool // 3`
(ranged) · `:1238` `(h_per_size + 1) // 2` · `:1521` `math.floor(LETHALITY_SCALE · …)` ·
`units.py:360` `total // TROOPS_PER_SIZE` · `:379` `math.floor(effective_size)` ·
`collective.py:117` `anchor_solo_pool // 2` · `faction_action.py:538`
`math.floor(W / MUSTER_WEALTH_TO_POOL_DIV)` · `mass_seizure.py:243` `int(ci) // POOL_CI_DIVISOR`.

### D — Threadwork's pool is integer three times over
`operations.py:145-157` — signature is `def _actor_pool(actor) -> int`, and inside:
`tps = ts // 10` (integer division), `history_contrib = min(3, history + 3)` (the inert cap, §7),
and an integer return annotation. Three separate integer-isms in one seven-line function.

### E — Display-only, no change needed
`wrapper.py:214, 306` — `round(net, 2)` / `round(net_sigma, 3)` inside `_emit(...)` trace calls.
Telemetry formatting, not resolution. **Leave them.**

### The two halves, and their asymmetric cost

**Half A — fractional pools.** Three lines (A above), then the C/D sites so nothing re-truncates
downstream. This is a **behaviour change**: it moves every seeded trajectory and re-records goldens.
Measured cost of *not* doing it (§1.2): the reward quantum stays at a whole die, ~+16pp, versus
+0.1D at ~+1.6pp.

**Half B — fractional obstacles, derived.** Strictly larger, and nothing has started. The ruling
says an obstacle is *the opposing actor's corresponding score ÷ 2, plus that instance's modifiers.*
Today **every** resolver passes a hand-set Ob: combat a fixed `DECISIVE_OB = 3`; contest a flat
`venue.base_ob`; threadwork/knots scale tables; mass battle alone uses the opponent's roll, and
there the degree is inert. So Half B is not a rounding fix — it is **the introduction of opposed
obstacles to a tree that has never had them**, and it changes what every difficulty in the game
*means*. It should be sequenced and gated on its own, not folded into Half A.

**Why this matters for §4's progression proposal:** with Half A done, `+0.1D` becomes a real
quantum. With Half B done, the obstacle becomes a *function of the opponent* — which is the single
biggest lever on mechanical distinctiveness in the whole tree, because it makes "who you are facing"
enter every roll, in every subsystem, instead of only in combat's `net_sigma`.

---

## §12 RELAY PASS — CORRECTIONS, AND THE CONCLUSION THEY INVERT

Agonist→antagonist relay per `CLAUDE.md` §10 (producers, then structurally-independent read-only
critics receiving only the producers' OUTPUT). **Three claims in §11 and in this session's reporting
were REFUTED.** They are corrected here rather than silently dropped.

### 12.1 REFUTED — "the opponent-derived obstacle is implemented nowhere"

§11 asserted this, citing `dice_engine.py:118-123`. **The docstring is wrong and §11 inherited its
error instead of measuring.** `systems/threadwork/sim/opposing.py:80-85` implements the ruled shape:

```python
def opposing_engagement_modifier(opponent_tps: int) -> int:
    return max(OPPOSING_OB_MODIFIER_MIN, opponent_tps // 2)
```

with `a_ob = base_ob + a_ob_mod` at `:120-140` — the opposing actor's score halved plus that
instance's modifiers — routed into the owner's ladder at `:95`. Live. `mass_seizure.py:258-268`
additionally derives an Ob from the contested entity's Prominence Tier.

**Consequence for the ruling: COMPOSE, do not re-derive.** ED-IN-0187's Half B has a working
primitive to build on. And the meta-finding is the more important one: `dice_engine.py:118-123`,
`test_degree_ladder_single_owner.py:38-41`, and this document all independently asserted the
primitive does not exist. **It is at active risk of being reinvented three scales over** — textbook
shape divergence (`CLAUDE.md` §10 guardrails).

### 12.2 REFUTED — "σ is a combat-and-contest-only channel"

`tests/sim/mass_battle/resolution.py` — the **J2 canon** mass-battle engine — self-describes as the
*"sigma-leverage head"* and exports `_morale_sigma` (`:107`), `_charge_shock_sigma` (`:161`),
`_sigma_softcap` (`:194`), `_sigma_net_boost` (`:206-210`). Morale and charge shock are carried as
δσ, soft-capped, μ-shifted — architecturally the same channel as combat. It takes **no `engine.*`
import by design**, which is exactly why an importer-graph survey misses it.

Also corrected: contest's σ is not "one 0.50σ setup advantage." `Leverage.net` puts the character's
own `faculty` into σ as `(faculty − 4)/6` (`primitives.py:227-230`) — a live distinctiveness channel
in σ, *in addition* to `faculty` entering the pool at `:211`. **`faculty` is double-dipped.**

**This inverts the design conclusion.** σ is the one advantage channel present at every scale that
has actually been built:

| scale | σ carries | site |
|---|---|---|
| personal combat | **all** opposition, against a fixed Ob 3 | `core.py:98-104` |
| social contest | `faculty` + armature alignment | `resolver.py:287`, `primitives.py:227-230` |
| canon mass battle | morale + charge shock | `tests/sim/mass_battle/resolution.py:107,161,206-210` |

> **Character distinctiveness expressed as pool dice is quantised and lossy; expressed as δσ it is
> continuous and survives.**

And the reason is *documented in the code as a judge finding*, not asserted: `resolver.py:279-282`
records that routing the armature through the pool turned a continuous 0.15 alignment into a
categorical 0.5-threshold step, because `roll_net` floors with `max(1, int(round(pool)))`; moving it
to the δσ μ-shift made it a real gradient. **This is ED-IN-0187's own argument, already made and
already won, inside one subsystem.**

### 12.3 REFUTED — "degree_from_net is single-owner by import"

Call sites are **eight in `systems/`** (§11 said six; it missed `mass_seizure.py:268` and
`systems/combat/sim/combat.py:171`), nine including `skills/valoria-dice-model/`. More importantly
the *property* is false: the J2 canon engine takes no `engine.*` dependency and its ladder
equivalence is held by **measurement, not an import edge** — stated at
`test_degree_ladder_single_owner.py:24-27`, whose own docstring (`:17`) says *"the tree does NOT
collapse to a single implementation and this file must not be read as claiming it does."*

### 12.4 Corrections of severity and novelty

- `units.py:299`'s missing `import random` is **unreachable** — `resolve_internal_collisions` is
  never invoked (`massbattle.py:1205`; named as the canonical dead-primitive example in
  `tools/dead_primitive_census.py:11`). Reporting it beside the **live** `CELL_PATTERN_FN` crash
  (`units.py:230`, reached from `massbattle.py:850` for any Arrowhead subunit) was the wrong
  severity signal.
- Threadwork's dead `BREADTH_OB`/`DISTANCE_OB` is **already recorded** in three standing instruments
  (`threadwork/_identifier_census.yaml:228-231`, the 2026-08-10 subsystem atlas, the 2026-07-29 dead
  primitive census). Presenting it as new inflated the audit's apparent yield.
- The contest's unimplemented `(Primary × 2) + History` is **already tracked as ED-SC-0004**, a P1
  blocker awaiting Jordan (`HANDOFF_SC.md:46`), with the identical finding in the 2026-08-06
  three-lens audit. Not a discovery. Sharpen: `ADJUDICATOR_PRIMARY` *is* read by the adapter
  (`wrapper.py:159` → `Contest.primary_attribute`) — just never by the resolver.

### 12.5 NEW — the strategic mass-battle path is geometrically degenerate

`_faction_to_unit` (`massbattle.py:1866-1894`) gives **both** sides `starting_position=(8, 12)` and
`advance_dir=1`. Identical shape + tier + position + direction ⇒ `Subunit.cells()` returns the same
cell set for both. Therefore: `find_contacts` (`:782-801`) admits distance 0, so the armies are in
full contact at tick 1 having never manoeuvred; and `advance_cells` (`units.py:181-191`) steers
toward the enemy centroid, which equals the unit's own, giving `dr = dc = 0` and a `continue` — so
**nothing ever moves.** Approach, facing, momentum, encirclement and the entire octagon-angle
apparatus are structurally inert on the wired path. The `[GAP:]` markers at `:1811-1813` and
`:1869-1872` disclose the stat defaults; they do not disclose the co-location.
`SIDE_A_START_ROW = 16` exists at `:60` as the canonical symmetric-deployment constant and is unused
here.

### 12.6 What survives, and what it means for the attribute question

The two most legible "this character is different" hooks in the tree are **Primary Attribute**
(metadata, never read by a resolver) and **tradition familiarity** (a pure function over a frozen
3-value table — `traditions.py:47-55`, confirmed: no state, no accumulation). **Neither is a place
distinctiveness currently lives, so neither is evidence about where it should.**

Where it should live, on this pass's evidence: **δσ**, because it is the only advantage channel
present at all three built scales, it is continuous where the pool is quantised, and the repo has
already litigated and won that argument once.

---

## §13 THE ACQUISITION-LAYER DESIGN FAILS — and the reason inverts §12.2

A concrete acquisition layer was designed for the contest kernel (schools + 20 grounded rhetorical
techniques mapped to lever sites) and attacked by an independent read-only critic. **It fails
structurally.** Recorded because the failure is the most useful finding of the pass.

### 13.1 The fatal defect: the policy layer cannot see the acquisition layer

`ContestView` (`contract.py:53-66`) is the **only** channel from resolution to decision — `_view`
builds it (`resolver.py:258-267`) and `Bout.resolve` passes nothing else (`:425`). Its twelve fields
carry ground, appeals, standings, `can_hard`, `reserve_frac`, turn index, `leading`, audience flags
and evidence count. **No field for a school, a technique, an invested level, or even the side's own
chosen Style** (`ArmatureConfig.styles` is a per-`Bout` constant, never surfaced).

Therefore **all 11 policies play identically with or without a school.** A school can only change
the outcome of moves the policy would have made anyway. That is a stat block, not an acquisition
layer — **the exact "who-bought-balance" degeneracy removed from combat on 2026-06-29
(`traditions.py:8-11`), re-entering through the front door under a new name.**

Combat's layer works because its levers sit inside *continuous per-event* resolution
(`bind_dominance_p`, `read_contest`, `grab_outcome`), which is why
`test_levers_add_texture_without_shifting_balance` can measure texture at all. The contest has **no
per-event trace** comparable to `run_traced_fight`. And transmission is quantised: `_advance` takes
`magnitude = deg ∈ {0,1,2,3}`, and at `faculty = 4` the Success band spans `2 ≤ net < 6.66` — twenty
graded abilities feeding a three-value quantiser across a band that wide change nothing, most of the
time.

### 13.2 ⚠ ED-IN-0187 INVERTS §12.2's CHANNEL ASSIGNMENT

§12.2 concluded distinctiveness belongs in δσ because the pool is quantised. **That conclusion is
conditional on the very rounding the ruling abolishes.** The δσ-over-pool argument rests entirely on
`roll_net`'s `max(1, int(round(pool)))` (`sigma_leverage.py:265`) — site A-1 of §11's census.

> **Execute Half A and the pool becomes the better lever: it is finer-grained (+0.1D ≈ +1.6pp vs
> +0.05σ ≈ +1.0–2.0pp), it scales with √pool rather than uniformly in z, and it needs no soft-cap.
> The channel assignment flips.**

§12.2 was stated with more confidence than the evidence supports. Corrected: **the right channel is
a function of whether the ruling is executed, and the ruling should be decided first.**

### 13.3 Lever census — most of the contest is dead

| lever | status | evidence |
|---|---|---|
| `rebut` magnitude | **DEAD on all 8 canonical proceedings** | `Venue.allow_rebuttal=False` (`resolver.py:163`); `proceeding_venue` never sets it. Where live, `min(REBUT_CAP, deg)` is inert at `deg==3` |
| CLASH / REINFORCE / CROSS / TIE | **DEAD — display only** | `derive_interaction` (`dictionaries.py:310-323`) has no resolver consumer; `agon_harness.py:458-462` says so |
| Doubt Marker / Obscuring-attacks-Face | **DEAD — a label** | `rhetoric.py:390-392`: *"a LABEL LOOKUP naming the ratified design intent"*; `_kernel_tests.py:1364` |
| `Pressure` / `_bias` | **UNREACHABLE** via `build_contest` | `proceeding_venue` never sets `pressure`; default `toward=None` ⇒ `_bias` returns 1.0 |
| `regroup` / `REGAIN` | **near-dead** | `min(self.max, …)` (`primitives.py:56`); past `REGAIN ≥ max`, exactly inert |
| pool magnitude < 0.5D | **silently inert** | judge finding 5 (`armature.py:54-59`) |
| `split_standing` | unreachable via canonical path | `resolver.py:162`, never set |

**Live and healthy, in order:** the δσ leverage term (`resolver.py:287`), the `gain` product
(`:315`), and `Standing.build`/`Room.build` (`primitives.py:35, 235`). **Put nothing anywhere else
until the dead levers are wired or struck.**

### 13.4 Two corrections to this document's own analysis

- **A bug the design would have shipped.** `resolver.py:343` refunds `Reserve.COST["evidence"]` from
  the **class constant**. A per-side cost-reduction ability spends `3·k` and refunds `3` — a reserve
  pump.
- **The `regroup` hazard was pattern-matched, not read.** It was flagged as a `1.30**level` overflow
  risk by analogy to combat's `value**level` crash (`ability_primitives.py:88-97`). `regroup` is
  `min(self.max, cur + REGAIN)` — clamped. The diagnosis was the **opposite** of the truth. Third
  instance this session of reasoning from a proxy instead of the code.

### 13.5 Measured, not asserted

- **Readiness headroom is +13.6% total.** `Readiness.of = 0.40 + 0.60·min(1, 0.40·sf + 0.40·rf)`;
  both fracs at 1.0 ⇒ 0.88. Raising `W_STANDING + W_ROOM` past 1.25 saturates the `min` and buys
  nothing.
- **The contest's "byte-identical" pin is weaker than claimed.** `_kernel_tests.py:1612-1618`
  compares **one derived float** with `isclose` over 40 seeds — the §0.1 point 2 anti-pattern
  (*"`pytest.approx` on an exactness claim … is not a weak test, it is an absent one"*). The right
  shape is combat's: an event-signature tuple compared with `==`
  (`test_combat_tradition_levers.py:130-147`).
- **The contest's fairness controls exist but are blind.** `_kernel_tests.py:127,150` assert mirror
  symmetry at `|a−b| < 0.07` / `< 0.06`; at N=2500 the per-side binomial noise is ≈±2.0pp, so the
  gate tolerates a genuine **±3.5pp seat advantage** without failing.

### 13.6 What this means for the recommendation

The §10.5 sequencing — *"build the acquisition tier for one non-combat system, then see which
attributes survive"* — **still holds, but its prerequisites are now known and they are not small**:

1. **Extend `ContestView`** so a policy can see its own school/kit. Without this, no acquisition
   layer in this kernel is playable, only purchasable.
2. **Build the instrument first** — position-swap (rebuilding the venue for role-asymmetric win
   conditions), Wilson CI, per-cell crc32 seeding, **policy-crossed and reported per-cell** (averaging
   over policies averages over *lever reachability*, since e.g. `logos_spammer` never emits an ethos
   move, so a Face ability measures exactly zero under it).
3. **Wire or strike the dead levers** before authoring content onto them.
4. **Decide ED-IN-0187 first**, because it determines whether the layer attaches to the pool or to δσ
   (§13.2).

---

## §14 THE ROUNDING FIX, PRECISELY — and a correction to §11's cost estimate

Jordan, reading the census: *"`roll_net` floors with `max(1, int(round(pool)))` — but that's an
integer rounding the pool."* Correct, and §11 conflated two separable things.

### 14.1 The floor is cited canon; the cast is not

```python
effective_pool = max(1, int(round(pool)))   # [canonical: params/core.md §Pool Floor (all systems)]
```

§Pool Floor says *"No penalty may reduce a pool below 1D."* **That authorises `max(1, …)` and
nothing else.** The `int(round(…))` is an **uncited integer quantisation riding inside a cited
floor** — which is how it survived: a reader checking the citation finds a real rule and stops.

Worse in `roll_net_continuous` (`:276-277`): it casts to `int`, then back with
`float(effective_pool)`, to call `continuous_engine_sample` — which accepts fractional pools
natively (*"Pool may be fractional"*). A float → int → float round-trip is **pure loss dressed as
continuity.**

### 14.2 Three measured facts

1. **It is banker's rounding, so the quantisation is not even uniform.** `2.5 → 2` but `3.5 → 4`;
   `8.5 → 8` but `9.5 → 10`. Half-integer pools jump by parity. This is the artifact behind §1.2's
   anomalous `+0.5D` row: pool 9.5 rounded *up* to a whole extra die.
2. **Stochastic rounding is mean-exact.** Roll `floor(pool)` dice plus one more with probability
   `frac(pool)`: measured 9.1 → 9.0997, 9.4 → 9.3999, 9.9 → 9.9001 (n=200k). A d10 engine that can
   never roll 9.1 dice can still honour a fractional pool honestly.
3. **The draw must be GUARDED on `frac > 0`.** Guarded, the RNG stream after integer-pool calls is
   identical to a fresh stream; unguarded, it shifts — re-recording every golden for nothing.

### 14.3 ⚠ CORRECTION — §11 overstated the cost of Half A

§11 said Half A *"is a behaviour change, not a repair — it moves every seeded trajectory and will
re-record goldens."* **Measured false.** Instrumenting `roll_net` across a live balance run:
**1,163 calls, every one at pool 9.0, zero non-integral.** `int(round(pool))` is a **no-op on every
call the live engine makes today** — which is precisely why the defect went unnoticed. It is dormant
until someone uses fractional pools, and then it silently eats them.

*Scope, stated not glossed:* that run exercises **combat only**, whose pool is integral by
construction at `core.py:52` (`int(round(history)) + BASE_POOL` returns an `int`), so the downstream
cast is redundant there. Other callers' pools were not directly instrumented.

### 14.4 The fix, per site

| site | change | cost |
|---|---|---|
| `sigma_leverage.py:276` `roll_net_continuous` | **delete the cast**; keep `max(1.0, pool)` as a float | none — pure removal, the callee already takes a float |
| `sigma_leverage.py:265` `roll_net` | **guarded stochastic rounding**: `n = int(p); frac = p - n; if frac > 0.0 and rng.random() < frac: n += 1; return max(1, n)` | none on existing content (stream-neutral) |
| `core.py:52` `resolution_pool` | drop `int(round(history))`; keep `max(POOL_FLOOR, …)` as a float | none until History goes fractional |

Then the §11-C sites (11 integer-only pool arithmetic sites) and §11-D (threadwork's
`-> int` / `ts // 10` / `min(3, history+3)`), each of which would re-truncate downstream.

**Write the diagnosis into the code at the fix:** the floor and the cast should never have shared a
line. A quantisation hid behind a citation long enough that three independent surfaces — including
`dice_engine.py`'s own docstring — ended up describing the tree wrongly.

---
---

# §15 NEXT-SESSION PLAN — SCAFFOLDING FOR PROGRESSION (no system chosen)

**Jordan's framing:** *build SCAFFOLDING for these progression systems; we are not necessarily
choosing one.* That is the right read of the evidence, and it is not a hedge — this session
established that **which** progression system is correct depends on decisions that have not been
made and instruments that do not exist. Scaffolding-first is therefore the only order in which the
choice can be made on evidence rather than taste.

**The governing insight for the whole plan:**

> Every progression alternative in §5 needs the same four things: a continuous resolution substrate,
> a place to put per-actor progression state, an instrument that can price a reward, and a channel
> to put the reward in. **None of the four exists today, and all four are system-agnostic.** Build
> them, and the choice becomes a measurement instead of an argument.

---

## §15.0 HOW TO RESUME

Read in this order. Do not start from this document's §7 (superseded twice — see §12, §13).

1. `CLAUDE.md` §0 and **§0.1** — the measurement discipline. §15.2 below is this session's evidence
   that §0.1 is not boilerplate.
2. `CURRENT.md` for currency; `registers/handoffs/HANDOFF_IN.md` for lane state.
3. **This document, in this order: §1 (what was measured) → §11 (the rounding census) → §14 (the
   precise fix) → §12 and §13 (what was refuted) → §15 (this plan).**
4. `engine/autoload/sigma_leverage.py` and `dice_engine.py` — the substrate everything sits on.
5. Only then the subsystem you intend to touch.

⚠ **Sections superseded within this document, do not act on them:** §7 (draft-1 recommendation,
withdrawn), §10.4's "put the budget in the acquisition layer" (that describes combat, which is
already done — see §10.5), §12.2's channel conclusion (inverted by §13.2).

---

## §15.1 THROUGHLINES TO CARRY

**Verified, survived adversarial attack:**

| # | Throughline | Evidence |
|---|---|---|
| T1 | **Attributes are absent from resolution in every finished engine.** Combat removed one (ED-901); contest never bound one (`faculty` is *"an abstract pool-size parameter, not Charisma"*). Two independent arrivals. | `core.py:50-52`; `primitives.py:128` |
| T2 | **Eight acclaimed games converged on the same rule: the attribute is a price or a rate, never a power.** DCSS, EVE, RimWorld, Battle Brothers, Darklands, WFRP, Blood Bowl, Dwarf Fortress. DF reached it under Valoria's exact posture (no GM, emergence). | §Appendix |
| T3 | **σ is present at all three built scales** — combat (all opposition), contest (`faculty` as `(faculty−4)/6` + armature), canon mass battle (`_morale_sigma`, `_charge_shock_sigma`). | `core.py:98-104`; `primitives.py:227-230`; `tests/sim/mass_battle/resolution.py:107,161` |
| T4 | **The acquisition layer is the real gap.** Combat has one (done); governance half-has one (Ledger tags, unconsumed); contest, threadwork, mass battle, fieldwork have none — and those four are exactly the four still leaning on attributes. | §10.5 |
| T5 | **Every engine consumes blends, never a bare attribute.** Reading, Reflex, Balance, Tempo, Impact, Durability, Concentration, Command. `balance_eff`'s comment generalises the architecture: *"BALANCE is NOT a stat (Jordan): it is GOVERNED BY AGILITY, modulated by CURRENT poise."* | `combat_systems.py:113-188` |
| T6 | **Deterioration is complete; the gain engine is absent.** Coherence, Scars, Knot rupture, demotion, collapse are all numerate and consistent. CP's spending menu cites a file that has never existed in this repo's history. | §1.5, §1.6 |

**Refuted this session — do not carry these forward:**

| # | Claim | Why it died |
|---|---|---|
| R1 | "The opponent-derived Ob is implemented nowhere" | `opposing.py:80-85` implements the ruled shape and is live. Three surfaces (incl. `dice_engine`'s docstring) assert otherwise — the primitive is at risk of a **fourth reinvention**. |
| R2 | "σ is combat-and-contest only" | The J2 canon mass-battle engine is a σ head; it takes no `engine.*` import **by design**, so importer surveys miss it. |
| R3 | "`degree_from_net` is single-owner by import" | 8 call sites, not 6; equivalence with the J2 engine is held by **measurement**, not an import edge. |
| R4 | "Distinctiveness belongs in δσ because the pool is quantised" | **Conditional on the rounding the ruling abolishes.** Execute S1 and the pool becomes the finer lever. §13.2. |
| R5 | "Combat's `familiarity` is durable memory" | A pure function over a frozen 3-value table. Nothing accumulates. |
| R6 | "Half A is a behaviour change that re-records goldens" | Measured: 1,163 live `roll_net` calls, all integral. The cast is a **no-op today**. §14.3. |

---

## §15.2 LESSONS — carry these harder than the findings

Every substantive error this session was caught by an independent critic, **none by me**, and they
were all the same error wearing different clothes.

1. **A proxy is not a measurement, and it can be anti-correlated with the truth.** §1.3's original
   grep-count "load-bearing" table **inverted** the real ranking: Strength grep-15 → +9.2pp;
   Cognition grep-2 → **+20.4pp**; Focus grep-4 → **+0.3pp**. Jordan's *"no pattern matching, no
   grep"* was a correct diagnosis of a live failure, not a style preference.
2. **The same error recurred three times** — grep counts, then an AST importer graph (missed the J2
   σ head, which takes no import by design), then transplanting combat's `value**level` overflow
   hazard onto `regroup` without reading `primitives.py:56`, where it is `min(self.max, …)` and
   therefore the *opposite* of an overflow risk. **When a method fails, suspect the method, not the
   instance.**
3. **Prose goes stale; re-run, don't re-cite.** The 2026-07-26 balance audit had `cog` exactly right
   and `history` off by 4.5pp. You cannot tell which without running it.
4. **Check that a citation covers the whole line.** `max(1, int(round(pool)))` carries
   `[canonical: §Pool Floor]`. §Pool Floor authorises the floor and **nothing else**; the integer
   cast rode in under it and survived for exactly that reason.
5. **Docstrings are inherited, including their errors.** `dice_engine.py:118-123` says the
   opponent-derived Ob "IS IMPLEMENTED NOWHERE." It is implemented in `opposing.py`. I repeated it
   as fact.
6. **Absence claims need a positive control.** The `valoria_ttrpg_complete.md` result held only
   because a known-present file was searched the same way in the same command.
7. **Attack the SETUP, not just the statistics** — §0.1's founding lesson, re-learned. Draft 1's
   adversarial pass checked the numbers and never asked whether the mechanism attached to a live
   lever. It did not: combat's Ob is fixed at 3.
8. **The relay works and is not optional.** Producer → independent read-only critic caught: two
   fabricated quotations, an inverted instrument, a refuted channel conclusion, a shipped bug
   (the `Reserve.COST` refund pump), and a structural blocker (`ContestView`). Budget for it.

---

## §15.3 THE SCAFFOLDING — seven stages

Each stage is **system-agnostic**: it is required by every alternative in §15.4. Each ships inert or
provably-neutral, each carries a falsifier, and none commits to a progression design.

### S1 — Continuous resolution substrate (executes ED-IN-0187 Half A)
**Why first:** it is the only work that changes *which channel a reward belongs in* (§13.2), and it
is measured to cost nothing today (§14.3).

| step | change | site |
|---|---|---|
| 1a | delete the cast; keep `max(1.0, pool)` as float | `sigma_leverage.py:276` |
| 1b | guarded stochastic rounding: `n=int(p); f=p-n; if f>0.0 and rng.random()<f: n+=1` | `sigma_leverage.py:265` |
| 1c | drop `int(round(history))`; keep float floor | `core.py:52` |
| 1d | the 11 §11-C integer-arithmetic sites + §11-D's threadwork trio (`-> int`, `ts // 10`, `min(3, history+3)`) | §11 |

**Falsifiers (all must pass):**
- **F-S1a** every existing golden byte-identical, and `pytest tests/valoria` unchanged.
- **F-S1b** RNG stream-neutrality: after N integer-pool calls the stream matches a fresh one
  (guarded passes, unguarded fails — demonstrated §14.2).
- **F-S1c** `p_success` strictly monotone in fractional pool across [5, 17].
- **F-S1d** stochastic rounding mean-exact: pool 9.1 → 9.100 ± 0.005 at n=200k.
- **F-S1e** a guard that fails on a *new* `int(`/`round(`/`//` applied to a pool or Ob — the §0.1
  point-5 recurrence guard. **If you cannot write this guard you have not understood the pattern.**

⚠ **1d is not free.** Fixing `min(3, history+3)` changes threadwork's pool by up to +3D
(≈ +1.2 expected net) and threadwork **has no oracle**. Gate 1d separately from 1a–1c.

### S2 — The obstacle substrate (ED-IN-0187 Half B) — **COMPOSE, do not re-derive**
`opposing.py:80-85` already implements *opponent score ÷ 2 + instance modifiers*. Promote it to a
single owner; make every other resolver able to call it; **correct the three surfaces that claim it
does not exist** (`dice_engine.py:118-123`, `test_degree_ladder_single_owner.py:38-41`, §11 of this
document).
**Falsifier:** the promoted owner reproduces `opposing.py`'s current outputs exactly; plus a guard
that fails on a new hand-rolled opponent-Ob derivation.
**Gate: JORDAN.** This changes what an obstacle *means* in every subsystem.

### S3 — The reward-pricing instrument
Before choosing a channel or a quantum, build the thing that prices a reward **in either channel**:
given Δ in {pool, δσ} at pool size N and Ob O, report marginal pp with Wilson CI at n ≥ 600.
**Known-answer control:** it must reproduce §1.1's attribute-parity table within CI.
**Why it is scaffolding:** every alternative in §15.4 needs to be priced, and none can be until this
exists.

### S4 — The contest instrument
`workbench/balance.py`'s method, ported: position-swap **with venue rebuild** (role-asymmetric win
conditions bind to the literal seat at construction), Wilson CI, crc32 per-cell seeding, **and
policy-crossed with per-cell reporting** — averaging over policies averages over *lever
reachability* (`logos_spammer` never emits an ethos move, so a Face lever measures exactly zero
under it).
**Control:** demonstrate that the kernel's existing `|a−b| < 0.07` mirror gate tolerates a genuine
±3.5pp seat advantage at N=2500.
**Do not author contest content before this exists** — that ordering is exactly how the "+2.8pp"
tradition-membership confound happened.

### S5 — Progression-agnostic state slots ← **the core of "scaffolding, not choosing"**
Define **where** progression state lives without saying what it is. Four slots, each shipping inert:

| slot | shape | precedent in tree | ships as |
|---|---|---|---|
| **Investment** | `{name: level}` on the actor | combat's `equipped` (`combatant.py:116`) | empty dict ⇒ factor 1.0 |
| **Practice** | per-domain **float** scalar | combat's `history` (currently int-quantised) | current value, float-typed |
| **Record** | durable, dedupe + TTL, survives succession | `settlements/sim/ledger.py` — the only real one | one owner; `familiarity` and `Dossier` become views |
| **Aptitude** | per-domain rate/price, **never in a pool** | none — this is the new slot | inert (rate 1.0) |

**Falsifier (and correct its known-bad precedent):** zero-investment must be **byte-identical across
≥40 seeds compared with `==` on an event-signature tuple** — as
`test_combat_tradition_levers.py:130-147` does. **Not** the kernel's `_kernel_tests.py:1612-1618`
shape, which compares one float with `isclose` and is the §0.1 point-2 anti-pattern.

Slots commit to nothing. They make every §15.4 alternative implementable as data.

### S6 — `ContestView` extension
Add school/kit/investment visibility to `contract.py:53-66`. Without it **no acquisition layer in
this kernel is playable, only purchasable** (§13.1) — the degeneracy Jordan removed in 2026-06-29,
re-entering by the front door.
**Falsifier:** a policy demonstrably behaves differently with vs without a kit. Demonstrated, not
asserted.

### S7 — Dead-lever disposition
**Wire or strike, before authoring anything onto them:** `rebut` (disabled on all 8 canonical
proceedings), CLASH/REINFORCE/CROSS/TIE (display-only, no resolver consumer), Doubt Marker
(*"a LABEL LOOKUP naming the ratified design intent"*), `Pressure`/`_bias` (unreachable via
`build_contest`), `split_standing`, `regroup` (clamped ⇒ near-dead), threadwork's
`BREADTH_OB`/`DISTANCE_OB`.
**Gate: JORDAN for the strikes** — several are ratified design text.

**Only after S1–S7: choose a system and author content.**

---

## §15.4 THE ALTERNATIVES, PRESERVED (so they are not re-derived)

Do not re-litigate these from scratch; they are costed in §5 and §3–§4.

**Character progression:** P1 Ledger/CP shop · P2 use-based sparking · P3 test-marking ·
P4 Pendragon traits+passions · P5 position-not-power · P6 entropy budget · P7 three clocks.
**Attribute rosters:** A-1 six faculties + two capacities · A-2 ratify the 10 · A-3 Focus derived ·
A-4 registry 9 · A-5 glossary 7.
**Faction:** F-1 ratify canon · F-2 Intel → Holdings ledger · F-3 split Mandate/Support ·
F-4 ~~Administration~~ (withdrawn — `ap × compliance` exists).

**Precedent shortlist that transfers** (§Appendix, and the §Precedent report): aptitude-as-price
(DCSS/EVE/Battle Brothers), school-as-price-tier not wall (WFRP: off-career costs **double**),
Netrunner **influence** as the non-degenerate cross-school budget, identity-as-named-objects at ~0pp
(Slay the Spire/CK3/Victoria 3), competence-gates-**information** (KoDP), continuous accrual +
quantised effect (EVE), attribute gains **rolled not chosen** (Blood Bowl d16).

---

## §15.5 DECISIONS THAT ARE JORDAN'S

**Blocking the scaffolding:**
1. **S2 — the obstacle substrate.** Changes what difficulty means everywhere. Nothing else in S1–S7
   waits on it, but content does.
2. **S7 strikes** — several dead levers are ratified text.
3. **S1d** — the threadwork `history_contrib` fix is a real behaviour change with no oracle.

**Not blocking (decide after the instruments exist):**
4. **OPT-AV-1, the roster.** §10.5's argument stands: the roster likely *shrinks* as subsystems get
   built, so ruling it now is premature exactly where it looks most needed.
5. **Which progression system** (§15.4). By construction, deferred.
6. **Focus** (+0.3pp, unread in threadwork) — cut, re-home, or give it a job.
7. **Charisma** — zero code; needs a resolution role or an honest demotion.
8. **Aging** — absent corpus-wide; raised, unanswered.

---

## §15.6 DEFECTS FOUND — independent of any design choice

| severity | defect | site |
|---|---|---|
| **LIVE CRASH** | `role_at_contact` references unbound `CELL_PATTERN_FN`; reached from `resolve_engagements` for any Arrowhead subunit | `units.py:230` ← `massbattle.py:850` |
| **HIGH** | Strategic mass battle is **geometrically degenerate**: both sides get `starting_position=(8,12)` and `advance_dir=1`, so contact is at tick 1 and `advance_cells` computes `dr=dc=0` — nothing ever moves | `massbattle.py:1866-1894` |
| **HIGH** | Threadwork History is inert: `min(3, history+3)` ⇒ pool 12 for history ∈ {0,3,7} | `operations.py:156` |
| **MED** | `massbattle.py` defines its own `roll_pool`, and it is **not equivalent off TN 7** (the owner ignores `tn`; this copy honours it) — latent divergence | `:627-638` vs `dice_engine.py:53-61` |
| **MED** | `tribunal.py` rounds an Ob that is already a float, then prints it as `%.1f` | `:119,122` |
| **MED** | `sim/conviction.py` runs a superseded 9-Conviction set; a live caller passes `'Loyalty'`, a member of neither set — silent no-op | `:42-49` |
| **MED** | Standing has **four** live ranges, one of them executable (contest kernel 0–10 feeding `Face_current`) | `clock_registry` 0–5, `faction_politics` 0–7, `player_agency` both, `primitives.py:121` |
| **LOW (latent)** | `resolve_internal_collisions` calls `random.randint` with no import — **unreachable**, a known dead primitive | `units.py:299` |

---

## §15.7 TRAPS

1. **Do not differentiate subsystems by attribute weighting.** That is FM24's architecture and its
   players' complaint. **Weighting masks are not an acquisition layer.**
2. **Do not revive a per-character channel-weight vector.** Removed 2026-06-29 as *"a degenerate
   who-bought-balance contest."* The failure mode is specific: *a free continuous allocation vector
   over a shared axis is always a solved optimisation.* Use a discrete priced budget (Netrunner).
3. **Do not put a sub-die reward in the pool while S1 is unexecuted** — `< 0.5D` is silently inert.
4. **Do not author onto a dead lever** (§15.7 list in S7).
5. **Do not build content before the instrument.** The "+2.8pp" retraction is the in-tree precedent.
6. **Do not reinvent the opponent-Ob primitive** — it exists; three surfaces say it doesn't.
7. **Do not let attributes be both the differentiator and the reward** — Oblivion's exact wedge.
8. **Do not trust a docstring, an audit, or this document over a run.**

---

## §15.8 WHAT WOULD MAKE THIS SESSION'S CONCLUSIONS WRONG

- **T1/T2 (attributes off the resolution surface)** fails if a built subsystem is found that
  consumes a bare attribute *and* is balanced. None was found; fieldwork and mass battle are
  unbuilt/degenerate respectively, so the sample is three engines.
- **§10.5's "attribute dependency is what a subsystem has instead of an acquisition layer"** is a
  pattern across six subsystems, four of which have no engine. **It is an inference, not a
  measurement, and it is falsifiable exactly once** — build S6+the contest layer and see whether the
  contest's attribute needs actually shrink. If they don't, the thesis is wrong.
- **§13.2's channel inversion** assumes S1 succeeds at zero cost. Measured for combat only.
- **The precedent convergence** is mechanism-level; two figures in the source report are flagged
  contested (CK3 Prowess conversion, WFRP bracket boundary) and are not load-bearing here.

---

# §16 THE EXPLICIT MAP — progression ↔ attributes ↔ systems

Measured by AST over `systems/` + `engine/`, reading **assignments** rather than references
(`CLAUDE.md` §0.1 point 1: *"grep the field's assignments — not its readers"*).

## §16.0 The measurement that governs the whole map

**Write sites for every per-actor quantity, excluding constructor self-assignment:**

| quantity | writers | quantity | writers |
|---|---|---|---|
| Strength · Agility · Endurance | **0** | History | **0** |
| Cognition · Attunement · Focus | **0** | Thread Sensitivity | **0** |
| Spirit · Recall · Bonds · Charisma | **0** | `equipped` · `skills` · `tradition` | **0** |
| Disposition | **0** | `faculty` | **0** |
| Renown | **0** | **Coherence** | **1** (`coherence.py:155`) |

And the three that *are* written are not what they look like:

- `crown.standing` (10 sites, `crown_initiative.py:115,118`, `absolution.py:86`) — a **faction's**
  standing, not a character's.
- `knot.strain` (2 sites, `knots.py:266,304`) — lives on the **Knot** object, a relationship, not
  the character.
- `state.coherence` (`coherence.py:155`) — **the only character-scale quantity any live code
  changes over time. It is a decay track.**

> **Every character quantity in Valoria is write-once-at-construction, except Coherence, which only
> goes down.** §1.6 called this "a complete loss engine and no gain engine" from the design texts.
> The write-side census is the stronger statement: **the gain engine has no write path at all.**

---

## §16.1 MAP A — attribute × system, by connection TYPE

`POOL` sizes the dice pool · `BLEND` enters a computed faculty · `GATE` is a threshold, never rolled ·
`CEILING` bounds a resource · `META` is carried by an adapter, never read by a resolver · `—` absent.

| | combat | contest | threadwork | knots/fieldwork | mass battle | factions |
|---|---|---|---|---|---|---|
| **Strength** | **BLEND** — Impact `Str+heft`; `½Agi+½Str` balance; bind; `0.25·Str·End` health | — | — | — | — | — |
| **Agility** | **BLEND** — tempo `K(agi−4)`; reflex; balance; footwork | — | — | — | — | — |
| **Endurance** | **BLEND** — `WI=End+4+0.4·Spi`; `stamina=3End+2Spi` | — | — | — | — | — |
| **Cognition** | **BLEND** — `reading=(2Cog+Att)/3` | **META** (`expert_judge`/`panel`) | **BLEND** — collective helper `⌊Cog/2⌋` | *(doc: Examine/Surveil/Cover)* | **BLEND** — `Command=⌈(2Cha+Cog)/3⌉` | — |
| **Attunement** | **BLEND** — reading (⅓), reflex | **META** (`no_adjudicator`) | — | *(doc: Interview/Read)* | — | — |
| **Spirit** | **BLEND** — WI, health, stamina, `conc=3Foc+2Spi` | — | **POOL** — `Spirit×2` + fatigue threshold | **POOL** — `Spirit×2` | — | — |
| **Focus** | **BLEND** — `conc_max`, `disrupt_resist`, `poise_regen` · **+0.3pp** | — | **declared, never read** | — | — | — |
| **Recall** | — | **absent** (CR6 names it; no consumer) | — | *(doc only)* | — | — |
| **Bonds** | — | — | — | **GATE** — `≥5`, count `⌊B/2⌋+1` | — | — |
| **Charisma** | — | **CEILING** — `Face_max=Cha×3` | — | — | **BLEND** — Command | — |
| — | | | | | | |
| **History** | **POOL** — `max(5,H+6)`, the *whole* pool | — | **inert** — `min(3,H+3)` | **POOL** — `+History(Rel)` | — | — |
| **Thread Sensitivity** | — | — | **POOL+GATE** — `⌊TS/10⌋`, gates at 30/50, **sets opponent's Ob** | **GATE** | — | — |
| **`faculty`** | — | **POOL + BLEND** — `faculty×2+3` **and** `(faculty−4)/6` into σ (double-dipped) | — | — | — | — |
| **`equipped`/`skills`/`tradition`** | **BLEND** — graded levers on σ components | — | — | — | — | — |
| **Disposition** | **BLEND** — commit skew, counter tilt, Vor drift | — | — | — | — | — |

**What the map shows:**
1. **Six of ten attributes touch exactly one system.** Str/Agi/End/Focus touch only combat; Bonds
   only knots; Charisma only contest+mass-battle.
2. **No attribute connects three or more systems.** Cognition connects the most (four, one of them
   `META`). The attributes are not a shared substrate — they are six private substrates.
3. **The columns disagree about what an attribute even is.** Spirit is a POOL in threadwork and a
   BLEND in combat. Charisma is a CEILING in contest and a BLEND in mass battle. There is no
   consistent semantics for "attribute" across the tree.
4. **The non-attribute rows are the load-bearing ones.** `History` *is* combat's entire pool;
   `faculty` *is* contest's; `TS` is threadwork's gate, pool term **and** the opponent's obstacle.

## §16.2 MAP B — the three-layer chain

Every system resolves through the same shape; they differ only in what fills the slots.

```
   ATTRIBUTE  ──►  FACULTY (computed)  ──►  CHANNEL  ──►  net  ──►  DEGREE  ──►  consequence
   (build-time)     (per-resolution)      pool | δσ
```

| system | attributes in | faculty computed | channel | Ob |
|---|---|---|---|---|
| combat | Str Agi End Cog Att Spi Foc | reading, reflex, balance, tempo, impact, durability, steadiness | **σ carries all opposition**; pool = History alone | **fixed 3** |
| contest | *(none — `faculty`)* | readiness, resonance, leak, room | pool **and** σ | flat `venue.base_ob` |
| threadwork | Spi (+Cog collective) | — *(no faculty layer)* | **pool only** | scale table **+ opponent TPS÷2** |
| knots | Spi Bon | — | pool only | fixed 2 |
| mass battle (canon) | Cha Cog → Command | morale, charge shock | **σ** | opponent's net |
| factions | *(none)* | — | pool = bare stat | hand-set 1–2 |

**The two structural facts:** the *faculty layer only exists in combat and contest*, and the
*obstacle is opponent-derived only in threadwork* (`opposing.py:80-85`) — the primitive ED-IN-0187
Half B should compose on.

## §16.3 MAP C — progression: declared vs actual

| quantity | design says it moves by | actual writer | status |
|---|---|---|---|
| Attributes ×10 | *"Advancement max 7"* | **none** | **no mechanism, no write path** |
| History | SaGa sparking; levels 1–3 | **none** | two incompatible models, neither implemented |
| CP | Belief/Duty/Domain-Echo at Accounting | **none** | menu cites a file never in this repo |
| Thread Sensitivity | grows with practice | **none** | gate + pool + opponent-Ob, frozen at creation |
| Renown | 8 sources, +2/season cap | **none** | fully specified, zero write path |
| Standing (character) | Duty ±1, Exceeding +2 | **none** *(the 10 writes are a faction's)* | four live ranges, no writer |
| `equipped` / techniques | graded investment | **none** | build-time input only |
| Disposition (per NPC) | −1/season decay above +2 | **none** | |
| **Coherence** | −1/op, banded, NPC at 0 | **`coherence.py:155`** | ✅ **the only live character loop** |
| Knot strain | ±, rupture at +5 | `knots.py:266,304` | ✅ live (relationship, not character) |
| Faction stats | 5 Stability triggers, income/drain | `crown_initiative`, `absolution`, `faction_action` | ✅ live at faction scale |

## §16.4 MAP D — the loops

**CLOSED (something changes, and the change feeds resolution):**
- **Coherence** → band → +Ob on future Thread ops → more failures → more Coherence loss. The one
  complete character feedback loop in the game, and it is a **death spiral by design**.
- **Knot strain** → rupture → Disposition −3, +1 Scar both sides.
- **Faction Stability/Wealth/Standing** → action pools → outcomes → stat deltas.

**BROKEN — writer exists, no reader:** Coherence *bands* are computed and persisted, but nothing
reads a band back into a pool or Ob outside threadwork; `COHERENCE_BAND_STRAIN_PACING` has no callers.
Settlement Ledger tags have **zero consumers** in `systems/`.

**BROKEN — reader exists, no writer:** *everything in §16.3's top eight rows.* Combat reads
`History` as its entire pool and nothing can ever change it. Threadwork reads `TS` three ways and
nothing can ever change it.

> **This is the precise shape of the problem: the systems are wired to READ progression state that
> nothing can WRITE.** The attribute roster question is downstream of that, and so is the choice of
> progression system.

## §16.5 MAP E — where progression would attach (the §15.3-S5 slots, per system)

| slot | combat | contest | threadwork | knots | mass battle | factions |
|---|---|---|---|---|---|---|
| **Investment** (`{name: level}`) | ✅ `equipped` exists | ✗ blocked by `ContestView` (§13.1) | ✗ none | ✗ none | ✗ `tactic_cards` = `{}` | ✗ none |
| **Practice** (float, per domain) | `history` — **int-quantised** | `faculty` — abstract | `history` — **inert** | `history_relationships` | ✗ | ✗ |
| **Record** (durable) | `familiarity` = static table | `Dossier` = per-bout | `CoherenceState` ✅ | `Knot.log` ✅ | ✗ | `ledger.py` ✅ *(unconsumed)* |
| **Aptitude** (rate/price, never rolled) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ |

**Reading the table:** the Investment slot exists once, the Practice slot exists but is quantised or
inert, the Record slot exists three times with **no shared owner**, and the Aptitude slot — the one
every precedent in §Appendix says should carry the attributes — **does not exist anywhere.**

That is the map. The scaffolding in §15.3 is exactly the work of filling the empty cells.

---

# §17 CORRECTION — attributes as formula inputs are FINE; three things were conflated

**Jordan:** *"Attributes inform/govern different functions. I don't see the issue with them able to
serve as input that define variable values in mechanical formulae."*

Correct, and §16.1 was wrong to present variety as incoherence.

## 17.1 WITHDRAWN — "the columns disagree about what an attribute is"

§16.1 called it a defect that Spirit is a POOL term in threadwork and a BLEND term in combat, and
that Charisma is a CEILING in contest and a BLEND in mass battle. **That is not incoherence, it is an
attribute governing different functions in different contexts — which is what an attribute is for.**
The POOL/BLEND/GATE/CEILING taxonomy is a *description*; presenting it as an indictment was an
error. Likewise **"six of ten attributes touch exactly one system" is specialisation, not a defect**
— Strength *should* matter mostly where bodies collide.

## 17.2 WITHDRAWN — the precedent conclusion had an unstated precondition

§15.1-T2 and §15.4 carried "attribute = price/rate, never power" from DCSS, EVE, RimWorld, Battle
Brothers, Darklands, WFRP, Blood Bowl and Dwarf Fortress. **Those games can afford to take attributes
off the resolution surface because they have DEEP skill systems** — DCSS runs 27 skill levels, EVE
five levels × hundreds of skills, DF unbounded combat skill — **carrying all the differentiation.**

Valoria has an acquisition layer in **one** subsystem. Therefore:

> **You cannot take attributes off the resolution surface until something else is on it.** In four of
> six systems nothing is, so attributes are currently the ONLY differentiator those systems have.
> Removing them would make the game less distinctive, not more.

The precedent transfer is **conditional on the acquisition layer existing first** — which is
§15.3-S5/S6, and is why the scaffolding is prior to the roster ruling. §15.1-T2 is corrected from a
recommendation to a *conditional*: it applies to a subsystem **after** that subsystem has a kit.

## 17.3 WHAT ACTUALLY SURVIVES — a weight-calibration defect, not an architecture one

Three separable things were flattened under one banner. Separated:

| # | finding | kind | status |
|---|---|---|---|
| 1 | attributes are inputs to mechanical formulae | **architecture** | ✅ **correct as designed — no issue** |
| 2 | the *weights* span 68× (`cog` +20.4pp → `focus` +0.3pp) while the creation points are fungible | **calibration** | ⚠️ real, and independent of progression |
| 3 | nothing can *write* any attribute | **progression** | ⚠️ real, and independent of both |

**Finding 2, stated precisely.** At creation, 31 points are freely allocable. Moving 2 points
(3 → 5, the creation cap) is worth ≈ **+41pp in Cognition and ≈ +1pp in Focus.** So **Cognition is
mandatory and Focus is a dump stat — at character creation, with no progression involved at all.**
That is a defect in the *coefficients*, fixable by re-weighting the formulae, and it touches nothing
architectural.

## 17.4 ⚠ AND FINDING 2 IS ITSELF CONFOUNDED — the same error a third time

The 68× spread is measured **in combat only**, because combat is the only fully built resolver.
An attribute whose home is elsewhere will *always* read as a dump stat under a combat-only
instrument. Focus's declared jobs are contest Concentration and threadwork ops-per-session;
Charisma's are Face and Command. **Those systems mostly do not resolve.**

So the honest statement is:

> **Attribute balance is not measurable until more than one system resolves.** A combat-only
> parity table cannot distinguish "this attribute is badly weighted" from "this attribute's
> subsystem is not built yet."

This is the §1.3 confound recurring in a new place — the third instance this session (grep counts,
importer graph, now a single-subsystem instrument read as a whole-game verdict). The one row that
survives the confound is **Focus**, because Focus is *also* declared-and-never-read in threadwork
(`operations.py:16`), so it has no unbuilt home to be waiting for. Charisma and Recall are genuinely
undecidable until contest and fieldwork resolve.

## 17.5 CONSEQUENCES FOR THE PLAN (§15)

- **§15.3 stage order is unchanged**, but its *rationale* is corrected: build the acquisition layers
  because four systems need a differentiator **in addition to** attributes, not as a replacement for
  them.
- **§15.5 item 4 is strengthened.** Ruling OPT-AV-1 now is premature for a second, independent
  reason: not only will the roster shrink or change as systems get built, but **the instrument that
  would justify any roster decision cannot exist until they do.**
- **§16.4's diagnosis stands unchanged** — the systems read progression state that nothing can
  write. That finding never depended on attributes being off the resolution surface.
- **New scaffolding item, S8 — per-attribute weight audit, deferred until ≥2 systems resolve.**
  The deliverable is a cross-system parity table, not a combat one. Until then, do not re-weight any
  attribute coefficient on combat evidence alone.

---

# §18 THE CHARACTER-FACING SURFACE — corrected map, and the allocation question

Jordan enumerated the surfaces and proposed a capability→surface mapping. Checked against code.

## 18.1 The missing surface: THREADWORK

Jordan's list — personal combat · mass combat as general · social contests · faction leadership
(faction actions) · settlement governance · field investigations — omits **Thread operations**
(Leap, Weaving, Pulling, Mending, Locking, Dissolution).

It is not a minor omission: it is **M1 juncture 5** (`valoria_master_workplan_v6.md` §1), it owns the
**only closed character feedback loop in the game** (Coherence → band → +Ob → more failure → more
loss, §16.4), and it is the **only subsystem where an obstacle is already derived from the opponent**
(`opposing.py:80-85`) — the primitive ED-IN-0187 Half B should compose on.

Two lesser candidates, raised not insisted on: **Knot formation** (its own roll, `Spirit×2 +
History(Rel)`, TN 7 Ob 2, where the degree selects a persistent *object type* — unique in the tree),
and **the Scene Slate triage itself**, which `player_agency_v30` calls the actual gameplay
(*"Choosing is the gameplay — not executing"*) without being a resolver.

## 18.2 The capability→surface map, corrected

| capability | Jordan's mapping | code says |
|---|---|---|
| **Physical** (Str/Agi/End) | direct: personal combat; secondary: field investigation, mass battle | **direct: personal combat — CONFIRMED** (15/8/4 read sites, all in combat). **Field investigation: by design only** (Endurance-exploration; the sim is `stub_resolve`). **Mass battle: REFUTED — no `strength`/`agi`/`end` read exists in `units.py` at all.** Command is `⌈(2Cha+Cog)/3⌉`, and `mass_battle_v30` states *"No mass-battle mechanic kills the general."* **A general's body is mechanically irrelevant.** |
| **Intellectual / social** | direct: leadership, governance, contests, field investigation, mass combat; secondary: physical combat | direct set **CONFIRMED** (Command = Cha+Cog; contest keyed Cog/Cha/Att by adjudicator; fieldwork Cog/Att/Rec/Cha/Bon). **"Secondary in physical combat" is INVERTED: Cognition is the single highest-value attribute in combat (+20.4pp), beating Strength (+9.2) and Agility (+6.3) 2–3×**, via `reading = (2·Cog + Att)/3`. Combat is already more intellectual than physical. |
| **Spirit** | primary: threadwork; secondary: all others | **CONFIRMED.** Threadwork's pool driver (`Spirit×2`) and fatigue threshold (`Spirit×5`); elsewhere only a secondary term (`WI = End+4+0.4·Spi`; `stamina = 3End+2Spi`; `conc = 3Foc+2Spi`); knots pool `Spirit×2`. Measured +6.0pp in combat — mid-table, the secondary signature. |

⚠ **Two surfaces read NO character attribute at all**: faction actions (bare faction stats — Mil, W,
I) and settlement governance (`ap × compliance`, Ledger tags). So of the seven surfaces, the
character sheet reaches five.

## 18.3 THE ALLOCATION QUESTION — measured

> *"The value of physical attributes depends upon how much of the game surface is spent in physical
> combat."*

This is the correct lens, and the measurement is stark. `engine/cross_scale/scene_dispatch.py:37`,
the dispatcher's own verification note:

> *"yet queues a combat scene either way (**verified 2026-07-29: no `queue_scene("combat", …)`**"*

The only `scene_type` the dispatcher queues is `"contest"` (`:86`). `DISPATCH_COMBAT_BRIDGE` defaults
**OFF** (`mc_v18.py:71,81`), and the note is explicit that the flag's state does not change this.

> **Personal combat is currently 0% of the generated game surface.** By the allocation argument,
> **physical attributes are currently worth ~0 of the character sheet** — not because they are
> badly weighted, but because the surface that consumes them is never generated.

**And this completes §17.4's confound.** The 68× attribute spread (`cog` +20.4 → `focus` +0.3) was
measured **in the one subsystem a campaign never enters.** An instrument aimed at a 0%-allocation
surface cannot price a character sheet. That is the third and largest instance of the session's
recurring error, and it is structural rather than careless: **combat is the only subsystem that *can*
be measured, which is precisely why every measurement drifts toward it.**

## 18.4 CONSEQUENCE — allocation is prior to weighting, and prior to the roster

Three questions, in the only order in which they are answerable:

1. **What is the surface allocation?** How many scene actions per season land on each of the seven
   surfaces. Today: contest ~all, combat 0, threadwork/fieldwork/governance unqueued. **This is a
   design decision nobody has made, and it sets every attribute's value.**
2. **What are the weights within each surface?** Only answerable per-surface, once ≥2 surfaces
   resolve (§17.4, S8).
3. **What is the roster?** Downstream of both.

**New scaffolding item, S9 — the surface-allocation budget.** Before any attribute weighting or
roster ruling, state the intended share of scene actions per surface across a season. It is the
denominator every other attribute question divides by, it is currently implicit and measured at
combat = 0, and it is a pure design call requiring no instrument.

⚠ **This also re-frames §1.1.** That parity table is not "the value of attributes." It is "the value
of attributes *conditional on being in a fight*", multiplied by a fight frequency that is presently
zero. Both factors are needed, and only one has ever been measured.
