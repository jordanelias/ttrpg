# Chapter 2 — The Ladder Runs Both Ways, On Paper

*Written at `571ae14` on branch `claude/fable5-valoria-proposal-analysis-fyi9jw`, 2026-08-25. Every
claim carries a `path:line` or is marked `[INFERRED]`/`[UNVERIFIED]`. I opened and read 27 distinct
locators at HEAD, parsed two registries with my own scripts, and executed two things: this chapter's
falsifier and `tools/m1_acceptance.py --summary`. One locator supplied to this run did not check out;
it is §9.1, not a footnote.*

---

## The claim

Jordan asked for officers, advancement *and* demotion, and internal competition inside factions. The
finding is not that these are missing. It is that **they are authored to unusual depth and wired to
zero**, and the wiring is smaller than the authoring already done.

- **74 rank rungs** across ten ladder tables, **every one carrying both an entry gate and a demotion
  cell** (my own recount, §2). The bidirectionality is real and, against the P1 dossier, rare.
- **Zero of those 74 execute in either direction.** No code fills a post, promotes, demotes, recalls or
  censures a named person.
- The substrate that would carry all of it — a five-kind relational tag ledger, a two-sided
  intra-faction contest running ~975 times per golden batch, a succession resolver, a
  governor-replacement primitive that already preserves durable consequences across the replacement —
  **is built and has no callers.**

So this is not a feature request. It is an argument about **which three writes, in which three named
functions**, convert an authored ladder into a running one; plus one live defect on the only
officer-adjacent number that *does* execute.

**Hard dependency, stated once.** Every recommendation involving a *named person* is gated on the
person loader, which **Chapter 1 owns**. I do not re-derive or cost it. What I own is what Chapter 1
leaves open: *once a person is loaded, what must an officer BE and DO?* Two of my three recommendations
(§8.1, §8.2) are deliberately independent of that loader.

**And the loader is not free — the run believed it was, and Chapter 1 refuted that by controlled
experiment.** The two guards everyone described as pinning the world's population pin `generate_npc`'s
**call counter** (`world.npc_counter`), not `world.npcs`. Loading two NPCs directly into `world.npcs`
left both guards green at `npcs_generated = 0` **and moved seed-42's winner from Crown to Hafenmark**;
a control arm with `simulate_npc_actions` neutered reproduced baseline byte-exact, identifying the
channel as `npe.simulate_npc_actions` drawing `world.rng` at `systems/overview/sim/accounting.py:139`.
**Populating the world moves seeded goldens unless season NPC drift gets its own RNG substream first.**
Chapter 1 owns this; every officer recommendation downstream inherits the cost, and §8.3 states it
where it lands.

---

## §0 — The correction this chapter owns: three Standings, and the one that is nobody's

The orchestrator claimed `Standing` was ratified 0–10 on 2026-07-08 and never executed, so the officer
ladder is "written against a scale that does not exist." The adversarial audit refuted it; the
orchestrator verified and retracted (`reports/L0g_RETRACTION_standing.md`). **The retraction is correct
and I re-verified all three mechanisms at HEAD.** It belongs in the published analysis: a document
warning that Valoria's central hazard is mistaking a shared word for a shared mechanism owes the reader
the fact that its own orchestrator did exactly that.

| | mechanism | shape | locator (verified) | executes? |
|---|---|---|---|---|
| **S1** | Contest ethos meter — per-bout, resets each contest, `build`/`strip` at 0.8/degree, clamped, feeds Readiness/leak and Face | `float`, `LO, HI, START = 0.0, 10.0, 5.0` | `systems/social_contest/sim/contest/primitives.py:31-48` | **yes** |
| **S2** | `Faction.standing` — durable per-faction modifier, ±1/±2 from Crown initiatives, Absolution, Parliamentary Transfer | `int = 0`, **unclamped** | `engine/autoload/game_state.py:129`; writes at `crown_initiative.py:98,116,119,167,177,254,267,270`, `absolution.py:86`, `parliamentary_transfer.py:379` | **yes** |
| **S3** | The officer rank ladder — 8 ranks, gates at Std 4/6/7, seven sub-office ladders | integer rank 0–7 | `systems/factions/faction_politics_v30.md:6,1141` | **no — prose** |

The ruling at `references/id_reservations_history.md:73` reads *"Standing range collision ratified (BG
faction track 0-10; **scope-tag the cross-scale homonym with the contest kernel**, OPT-AV-12; FA
co-sign); execution pending."* That preserves the homonym and asks for it to be **labelled**. The
unexecuted work is *tagging*, not *rescaling*.

Two further prose senses contradict each other inside one CANONICAL file:
`systems/_architecture/player_agency_v30.md:365` ("The Standing ladder runs 0–7") versus `:406`
("Standing (0–5)"), 41 lines apart, both verified. `systems/overview/clock_registry_v30.md:53` declares
the BG track 0–5. `crown_initiative.py:260` records that the pairwise "Standing-with-X" sense is *"not
modeled."*

### §0.1 The real defect, sharper than "unclamped"

L0g's replacement finding — `Faction.standing` is an unclamped int read into a dice pool, a NERS-R
failure — is right, and worse in two ways it did not state.

**There are two pool reads, not one.** `crown_initiative.py:81` (`pool = int(crown.I) + crown.standing`)
and again at `:309`. The outcome of each roll writes standing back (`:98,116,119` off `:81`;
`:254,267,270` off `:309`). Two closed positive-feedback loops, no damper on either.

**And `standing` is not merely unclamped — it is not a faction descriptor at all.** Executed:

```
>>> sorted(descriptors.FACTION_STATS.keys())
['fac.influence','fac.intel','fac.legitimacy','fac.military','fac.stability','fac.wealth']
>>> descriptors.faction_bounds('standing')   →  None
>>> game_state.MULTS   →  {'L':20,'Sta':10,'W':100,'I':15,'Mil':10,'accord':10,'pt':10}
```

The ratified roster is six (`descriptors.py:78-94`; Jordan's 2026-08-23 "Legitimacy is a base" closed
the L gap). `standing` is a **seventh durable per-faction number outside the descriptor system** — which
is exactly why every write is a bare `+=` and not `Faction.adjust()`. It could not use `adjust()`:
`MULTS` has no `standing` key, so the call raises `KeyError` at `game_state.py:59`, as that function's
own docstring warns for `intel`.

**This changes the fix.** "Clamp it like the others" is unavailable: there is no registry row and no
ratified range — 0–5, 0–7 and 0–10 belong to three different mechanisms, and picking one would be the
exact pattern-match this run exists to prevent. Options in §8.1.

**What survives about the ladder.** Under §0.05 its numbers are **not "written against a nonexistent
scale."** They are **not a mechanism yet.** Smaller claim, truer one, and the basis for the rest.

---

## §1 — Officers: is there an officer object?

> **Verdict: No. There is no officer object in executing code. The nearest thing is a nullable string
> on `Settlement` that nothing ever sets, plus a 46-record authored cast no runtime module opens. The
> officer system must be built, not repaired.**

`Faction` is `name / parliamentary / L / Sta / W / I / Mil / intel / territories / standing` plus
seasonal flags (`engine/autoload/game_state.py:109-137`). **No member list, no leader field, no office
slots** — and `parliamentary_action.py:69-71` says so in its own voice, having had to justify a targeting
heuristic without one: *"No grudge / hostility / inter-faction-relationship stat exists in
game_state.Faction … the Faction schema is L/Sta/W/I/Mil only."*

`Settlement.governor_id: str | None = None` (`systems/settlements/sim/registry.py:61`) is the only
post-holder field in the tree. Grep across every `.py`: **five** hits — declaration, `to_dict`,
`from_dict`, one assignment inside `succeed_governor`, and a docstring at `:237` explaining that
`populate_from_geography` deliberately leaves it unset. `succeed_governor` (`registry.py:199-208`) has
**zero callers**. In every seeded campaign, no settlement has ever had a governor.

The declared officer Key vocabulary is consumer-side only. `state.coup_attempted`, `state.succession`
and `da.covert_betrayal` sit in articulation's trigger roster (`engine/cross_scale/articulation.py:118-120`)
with **no emitters**; `state.standing_change` and `officer_deaths` return **zero `.py` hits at all**.
(That is Chapter 1's T-01 pattern; I cite rather than re-derive, noting only that the officer
vocabulary is one of its purest instances — three of the four Keys that would carry a career event are
subscriptions to nothing.)

### §1.1 The cast is data, and the data has a defect

I parsed `references/npc_registry.yaml` rather than reading it, which **partly corrects this run's own
brief** (which described 46 officeholders carrying "role, title, faction, territory, stats and goals"):
of 46 records, `role` 46, `faction` 46, `arc_trajectory` 36, `goals` 17, **`title` 7, `territory` 7**.
The universal fields are two free-text strings. Runtime readers: **none** — the only `.py` naming the
file is `tests/valoria/test_references_yaml_parse.py`.

**A defect the loader will ingest.** Two records carry a YAML comment marker inside an unquoted scalar:

```
references/npc_registry.yaml:835    faction: Hafenmark (Inner Council #4)
references/npc_registry.yaml:850    faction: Varfell (Jarl Council #5)
```

`#` opens a comment, so these parse as `"Hafenmark (Inner Council"` and `"Varfell (Jarl Council"` —
silently truncated. NPC-081 and NPC-082 land in two singleton namespaces no other record shares, while
`"Hafenmark (Inner Council)"` and `"Varfell (Jarl Council)"` (`:742,756,770,784`) hold the other four.
Invisible to reading, found by parsing. Two characters to fix, and it must land **before** any loader,
or the first four officeholders instantiated belong to four different bodies than the author wrote.

The truncated text is the better finding: **`Inner Council #4` and `Jarl Council #5` are seat numbers.**
The registry is encoding a numbered seat in a free-text faction string because there is no seat object.
That is the officer object trying to exist inside a `str`.

### §1.2 What an officer must BE

**An office-binding, not a stat block.** The corpus's own clearest statement is the role table splitting
six skill roles from four position roles: attributes "cannot distinguish these roles, and were never
going to … they are distinguished by practice, instruments, and **office**" — "General **and an army** ·
Politician **and a seat** · Governor **and a settlement** · Leader **and a faction**" (via
`reports/L1_proposals_aug15_19.md §E-1`).

The *shape* of the corps is constrained by P3 §2.2's Band of Blades split: **a small fixed set of
mechanically distinct seats above an explicitly fungible pool**, whose aggregate state is what the named
seats decide against. That is the anti-scripting-drift shape for a no-GM design, and it is load-bearing:
deaths in the pool need no narration to matter, because they only move an aggregate the seats read.
Valoria has the aggregate side (per-cell morale is the mass-battle primitive,
`systems/mass_battle/sim/hierarchy/units.py`) and no named seats.

Minimum officer record: **a typed seat** (small enum, not a free-text role string), **a holder** (person
id, nullable — vacancy is a state, not an absence), **a rank on that seat's ladder**, **a patron edge**,
**an advance predicate reading live state**. Four of five are sketched in the PROPOSED Ascendancy sheet
(`power_base`, `consolidation_progress`, `patron_id`, two-axis loyalty, `succession_eligible`)
[UNVERIFIED — I take L7's extraction of the archived §40.2.3, not the file]. `power_base` and
`patron_id` return **zero `.py` hits**.

And the thing an officer must *do* that matters most is §3's: want something its faction does not.

---

## §2 — Advancement and demotion: does the ladder run both ways?

> **Verdict: On paper yes, and unusually well — I independently counted 74 rungs, each carrying both an
> entry gate and a demotion cell, plus ≥15 cross-cutting downward mechanisms. In code the officer ladder
> runs zero paths up and zero down. The only executing "standing" is a per-faction scalar with five write
> sites up and five down, which is more bidirectionality than any character ladder has, and belongs to
> no person.**

### §2.1 The count, recounted

I parsed the ladder tables rather than trusting L7's ~74. Every table in `faction_politics_v30.md` with
a `Demotion` column: the four primary ladders at `:155, :212, :250, :323` (8 rows each = 32), plus
Löwenritter `:389` (8), Riskbreakers `:412` (7), Inquisitors `:512` (6), Templars `:531` (6), Guilds
`:552` (7), Wardens `:625` (8) = **74 rungs, each with a gate cell and a demotion cell.** L7's 74
reproduces exactly; its 88 up-gates is the 64 in-table gates (a Std-0 row has no gate into it) plus the
informal Niflhel path and the alternates.

Above the rungs sit ≥15 cross-cutting downward mechanisms, seven of which I verified individually:
§1.0a Demotion Magnitude (default −1, severe −2/−3, total failure → Standing −1 plus a Dishonored flag,
`faction_politics_v30.md:59-94`); a two-season appeal window with no appeal for Dismissal (`:92`); the
Riskbreaker Deniability-Debt cap, which demotes the commander and drops *every* Rb rank by one
(`:486-497`); Conviction Reformation failure (`:739-748`); the Baralta cascades (`:863-921`); a failed
leadership challenge dropping the challenger to Standing 2 (`player_agency_v30.md:388`); and §6.4's
battle-fate table (`faction_layer_v30.md:599-614`). Few games in the P1 dossier have a down-direction
this developed.

### §2.2 Executed: zero — and what *is* executing is the template

| path | dir | executes? | locator (verified) |
|---|---|---|---|
| Parliamentary Censure — target `Sta −1`, `L −1` on pass | down | **yes** | `faction_action.py:276-301` → `parliamentary_action.py:97-160`, effects `:154-158` |
| Parliamentary Transfer, Punishment-mode failure — `holder_fac.standing -= 1` | down | **yes** | `parliamentary_transfer.py:379` |
| Crown Initiative outcome bands | both | **yes** | `crown_initiative.py:98,116,119,167,177,254,267,270` |
| Church Absolution failure — `church.standing -= 1` | down | **yes** | `absolution.py:86` |
| `succeed_governor` — replace an officeholder | lateral | **no** (0 callers) | `registry.py:199-208` |
| every rung of every ladder | both | **no** | `faction_politics_v30.md` Parts 1–2 |

Note the censure path's shape: the **only** demotion in the game *proposed by an agent, adjudicated by a
body, and applied to a target*. It self-gates (GD-3 + proposer Mandate ≥ 2), picks its target by an
explicitly non-fabricated heuristic grounded in Athenian ostracism (`parliamentary_action.py:76-83`),
runs a real ballot, applies a two-stat effect. **That is the officer-demotion pipeline, already built,
one scale too high.** Re-pointing it at a seat is smaller than authoring one.

### §2.3 What does a demoted officer DO?

The 74 demotion cells do not say, and P1 shows answering it wrongly is the standard failure. Two
precedents pull opposite ways and both must be carried.

**P1 §A1 (CK3's landless-adventurer track): demotion must be its own game, not a debuff.** A demoted
officer that merely loses bonuses is a subtraction, and subtractions are not play. The state needed is
"a game-mode/action-set flag per Standing band, not merely a multiplier on existing actions."

**P1 §9.4 (Dwarf Fortress's counter-warning): demotion with no residual reads consequence-free once
survived.** A comeback that resets to zero is a reset button.

Both are answered by one object: **the demoted state must carry tags forward** — a Grudge against
whoever demoted them, Leverage they retained.

**And Valoria has already implemented the residual, with zero callers.** `succeed_governor` does not
merely swap a string; it calls `ledger_sweep(s.ledger, season)` (`registry.py:207`), and `ledger_sweep`
is *"Remove expired (ttl) tags; durable tags (ttl=None) always survive"* (`ledger.py:69-75`). The five
kinds are `{"Precedent","Grudge","Debt","Reputation","Leverage"}` (`ledger.py:30`), `Reputation`
single-valued because it is "a single read of the governor — latest wins."

**So the succession primitive Valoria will need already guarantees the exact property P1 says Dwarf
Fortress lacks: the durable record of what a governor did survives the governor.** It has never run.
Missing is (a) a caller and (b) any tag writer at all — `add_tag`/`ledger_add`/`LedgerTag(` outside the
two owner modules: **zero hits.**

**Minimal spec for the demoted officer's own game.** Retain (i) durable ledger tags at settlements
governed — free, `ledger_sweep` already does it; (ii) a `Grudge` keyed to the agent whose action demoted
them, written at the moment of demotion; (iii) an action set gated on a **band**, not an exact rank —
P1 §A4's Shogun 2 lesson is a **visible band over a hidden precise value**, which is what keeps the
down-direction from reading as arbitrary. Three bands suffice: *seated*, *displaced* (no post, rank
intact, may contest), *dishonored* (§1.0a's Dismissal, no appeal per `:92`).

**One arithmetic discipline, from P1 §B1, binding on the next number anyone tunes here.** Imperator:
Rome's launch loyalty dropped "no matter what players did" — governors lost 20+ on appointment alone;
the fix cost a full currency rebuild four months later. **Test the down-direction's arithmetic against
the best-case counter-investment, not the average case.** If the fastest mitigation still nets negative,
the mechanic is broken, not hard. Valoria's §1.0a magnitudes have never been checked this way; they come
from a 2026-04-25 stress test with no precedent cited (§7).

---

## §3 — Internal competition: does any executing code model an agent whose interest diverges from its own faction's?

> **Verdict: No. Five lanes said no independently and I re-verified their three nearest primitives at
> HEAD. But "no" is the wrong shape of answer. The divergent-interest *contest* already executes on the
> default campaign path ~975 times per golden batch. What is missing is not the contest, the trigger,
> the resolver or the consequence. What is missing is that neither side is anybody.**

### §3.1 The three near-misses, verified

**(a) `NPC.hidden_allegiance` — computed and dropped by the constructor.** At
`systems/world/sim/npe.py:327`, inside deviation branch `flip_choice == 2`:
`hidden_allegiance = rng.choice(other) if other else None`. The constructor immediately below
(`:336-347`) passes ten kwargs and **not `hidden_allegiance`**; the field defaults to `None` (`:137`).
One of five deviation branches is a silent no-op that consumes an RNG draw and writes nothing. Grep:
declaration, serialize, deserialize, this dead write. **Zero reads.** (CLAUDE.md §0.1 pt 2 in the wild:
a test asserting the draw happened would pass; nothing asserts the effect landed.)

**(b) The ledger's rivalry vocabulary — real schema, no writer.** `TAG_KINDS` (`ledger.py:30`) contains
exactly the intra-faction rivalry primitives; `Settlement.add_tag` (`registry.py:100`) has zero external
callers. This settles a design question: **every Grudge/Debt/Leverage key authored anywhere in the
corpus is already intra-polity** — `Leverage:konrad-corrupt`, `Debt:harbor-corrupt-agent`, governor ↔
local actor ↔ Crown agent inside one Crown settlement. The substrate's intended first use *is*
intra-faction rivalry. It has no writer.

**(c) `contest/faction.py::succession` — executes only under its own kernel tests.** At
`systems/social_contest/sim/contest/faction.py:86-119`: two claimants **within one faction** contest
leadership on the Persuasion Track, returning `unified`/`decisive`/`split` with §7.2.1 ratios
0.60/0.55/0.50 and a Verdun-843 grounding annotation at `:106-115`. Callers by grep: its own
`succession_rate` helper and `_kernel_tests.py:179`. **No production call site, and none reachable** —
`Faction` has no leader field, so leader elimination is not an event the season loop can produce.

Also verified: `Settlement.legitimacy`/`popular_support` (`registry.py:74-75`) are declared, serialized,
and never read or written by any logic — S→F is PROSE-ONLY exactly as the matrix marks it.

### §3.2 The better answer: the shape exists, the people don't

`engine/cross_scale/scene_dispatch.py:121-139` is `_emergency_council_parties`. Fired by the Stability
Crisis trigger, it derives **two internal sides of one faction**:

```python
return (max(1, round(f.L)), max(1, round(7.0 - f.Sta)))
```

`side_a` is "the sitting leadership's case to stay the course"; `side_b` "the crisis's own case for
change." This runs on the **default** path — `ECHO_TRANSPORT` is default-ON with Jordan's 2026-07-08
ratification quoted in the flag's own docstring (`engine/mc_v18.py:63-77`) — and
`engine/tests/test_f7_smoke_oracle.py:275` pins `GOLDEN_SCENES_RESOLVED = 975` over the 8-campaign
seed-42 batch.

**Valoria already ships an intra-faction two-sided political contest with a real resolver, a real
consequence, and ~1,000 firings per golden batch.** It is degenerate in three verified ways: both sides
derive from the same faction's aggregates (`L` and `7 − Sta`); both are played by the same policy
(`logos_spammer` vs `logos_spammer`, which the module notes at `:311-313` makes every verdict
deterministically Memory-genre); and the echo returns to the faction it came from — `ctx["echo"] =
{"actor_faction": winner_fid, "target_faction": winner_fid, …}` (`:267-268`), with the code stating why
at `:331-332`: *"Both sides of this contest are the SAME faction's own facets, so
actor_faction==target_faction."*

A faction arguing with itself, both sides from its own stats, resolved by two copies of one policy,
echoing onto the stat it came from.

### §3.3 The socket nobody found

`_emergency_council_parties` returns **two bare ints**. The adapter receiving them,
`systems/social_contest/sim/contest/wrapper.py::_as_contestant` (`:80-96`), accepts three shapes — a
`Contestant`, an int/float faculty, or **a dict**:

```python
if isinstance(side, dict):
    faculty  = int(side.get("faculty", 4))
    standing = float(side.get("standing_start", Standing.START))
    ...
    return Contestant(faculty, standing_start=standing, dossier=dossier)
```

Because ints are passed, both sides take the int branch and both get `standing_start = 5.0`. **The
kernel already accepts a per-side starting standing and a per-side evidence dossier. The
party-derivation function declines to supply them.**

Behind it sits a deeper socket. `Venue.split_standing` (`resolver.py:162`) is a default-off prototype
splitting the fused contest Standing in two:

```python
self.rank   = Standing(spec.standing_start)  # ascribed station: gates the hard-tactic gradient; not built by ethos
self.credit = Standing(Standing.START)       # earned credibility: built by ethos/support
```

(`resolver.py:204-205`.) **`rank` is "ascribed station"** — a purpose-built slot for a station a
contestant walks in holding, which the bout cannot manufacture or inflate. That is precisely and only
what an officer's ladder rank is.

This is a genuine class-(a) throughline: **state one mechanism writes that another reads.** The ladder
writes a rank; `standing_start` reads one; `split_standing` gives it a non-ethos-built channel. Not a
shared word — S1 and S3 remain a vocabulary collision as a matter of *identity*, and unifying their
ranges would still be §0's error. It is a **feed**: the ladder is not the contest meter, it is an
*input* to it, which is the relationship the 2026-07-08 scope-tag ruling anticipated.

### §3.4 What a divergent interest must BE, mechanically

For a GM-less engine to act on divergence it needs four things; Valoria has partial versions of all
four.

1. **A persistent holder** — a person, from Chapter 1's loader. *Missing.*
2. **A payoff that is not the faction's.** The mandated primitive from L4 §D.1's F9 bloc slice is a
   **`benefit-when-faction-loses` flag**: a bloc whose payoff is negatively correlated with the
   faction's headline outcome — a war party that gains from a lost peace. Cheapest possible divergence:
   a boolean and one sign flip in a payoff read. *Missing, and it is one field.*
3. **A decision that reads it.** Divergence no selector consults is `hidden_allegiance` again. The read
   belongs at an action-selection site; `faction_take_action`'s dispatch (`faction_action.py:276-301`)
   is the one that exists.
4. **A record that outlives the decision.** The ledger tags, which already survive succession by
   construction (§2.3). *Built, unwritten.*

The generator invariant L4 §D.1 states is right and I endorse it verbatim: **every faction must carry
≥1 bloc pair such that any Directive it issues pleases one bloc and wrongs the other.** That is the
faction-scale transposition of Goldenfurt's central rule — *"Hedda (law) vs Orsk (commerce) is the
central rivalry — any `Hold Court` ruling pleases one and wrongs the other"*
(`systems/settlements/goldenfurt_slice/npc_cast.md:29`). An invariant, not a scripted rivalry, which is
what keeps it clear of scripting drift.

For the *gate* on acting against a bloc, bind P1 §A2 (EU4 Estates): track **Loyalty** and **Influence**
separately, gate revocation on Loyalty > Influence — "you may only revoke what you can afford to lose" —
with a spillover rule making over-empowerment systemic rather than local. Its attached warning is not
optional: Estates are *the single most commonly reported "safe to ignore" mechanic in the whole
dossier*, because the loyalty floor sat near 40 and nothing ever crossed it. **Tune the thresholds to
fire on a normal timeline or cut the mechanic** — and per §0.1 pt 4 the tuning needs a control arm in
which it is deliberately never engaged.

---

## §4 — The G606 / §1.0d verification, and its resolution

**The verification.** Verbatim from the working tree, `systems/_architecture/ners_vsg_reconciliation_v1.md:40`
(row D5):

> `pr119_integrated_campaign.py`, 3 regimes × 500 trials: G606 (cumulative suspicion) drives **100% of
> terminal recalls in the most lenient §1.0d tuning tested** — leniency tuning on §1.0d doesn't move the
> outcome at all, because G606 alone is sufficient and dominant.
>
> Verdict: **CONFIRMED**, and sharpened: this isn't "§1.0d duplicates G606," it's "§1.0d currently
> contributes ~nothing once G606 is live"

**Both still live? Yes.** §1.0d stands at `faction_politics_v30.md:129-143`, `Status: PROPOSED …
promote-ready`. G606 stands at `systems/settlements/governance_play_redesign_v1.md:115-125` (Comply /
Bargain / Defy, "suspicion track +1; at threshold → recall, audit, or replacement") and
`npc_cast.md:100-111` (Konrad's autonomous advance, "+1 each season you Defy or Bargain… cap +1/season").
The merge is **ruled** (D5) and tracked explicitly unexecuted. **The live design carries, in two
documents, a mechanism measured to contribute approximately nothing, alongside its ruled replacement.**

**The harness is not re-runnable.** `pr119_integrated_campaign.py` exists in neither the live tree nor
the recovered archive (I searched the filesystem). The 100% figure is **quoted, not reproduced**.

**Which is why the resolution should not rest on it.** The archived README gives the *mechanism*, and
the mechanism is checkable by arithmetic:

> even with a gentle governor (75% compliant) and a lenient **5-consecutive-miss** §1.0d threshold …
> 100% of terminal recalls route through G606 (0 via `performance_audit`) — because G606's progress is
> **cumulative, not streak-based** (capped +1/season, **fires at ≥4**) … §1.0d's own streak-reset design
> (a single Comply resets `pa_streak` to 0) makes it the FORGIVING mechanic here.
> — `archived/audit/2026-07-12-pr119-harness-verification/README.md:100-112`

**Read arithmetically, the empirical result becomes a theorem.** G606 is a **cumulative counter, cap
+1/season, firing at 4**. §1.0d is a **streak counter reset by one compliance**, threshold 5 in that
regime. Five consecutive misses contain five total misses, and G606 fires on the fourth. **Under that
tuning §1.0d cannot fire first on any trajectory whatsoever** — 100% is a certainty, not a statistic,
and no number of trials could have shown otherwise.

Generalised: with cumulative threshold `c` and streak threshold `k`, §1.0d fires strictly first **only**
if `k < c` *and* the first `k` misses are consecutive. For `k ≥ c` its marginal contribution is exactly
zero for every trajectory and every compliance rate; for `k < c` it is bounded above by the probability
of an unbroken opening run of length `k` (at most `p^k` for non-compliance rate `p`), and on those
trajectories G606 sits at `k` and follows within `c − k` further misses. [INFERRED — my derivation from
the two mechanisms' stated shapes, not a re-run.]

**So the resolution is stronger than "merge them because the data says so."** *A cumulative accumulator
and a streak accumulator reading the same signal are not two mechanisms.* §1.0d is not under-tuned; it
is **structurally redundant with any cumulative sibling**, and tuning was never going to reach it. A
NERS-N failure of the cleanest kind: a mechanism whose contribution is provably zero.

**Do the merge (D5), and carry the two things it does not settle.**

- **D6, the wiring fork, is the sharper lesson** (`ners_vsg_reconciliation_v1.md:65`):
  clock-advances-every-non-compliant-season → recall dominates near-totally; advances-only-on-a-card-draw
  → recall cascades effectively never fire even at 30 seasons. **"Two meaningfully different felt games,
  not two implementations of one spec."** State it as a design law: **a throughline template
  underdetermines the felt game until its clock-advance predicate is fixed.** Advance predicates are not
  implementation detail.
- **E11, symmetric suspicion decay, is a ruled co-requisite authored nowhere and coded nowhere.**
  Without it the merged signal is a one-way ratchet — accrual with no recovery, a NERS-R failure and
  precisely P1 §B1's Imperator shape (a down-direction the agent cannot out-invest). **The merge must
  not land without a decay term in the same commit.**

One thing the design already gets right and must not lose: G606's escape hatches. Konrad's *Secret: he
takes Orsk's coin* is "corruptible, and discoverable via `Investigate` — **your counter-lever against
the suspicion track**" (`npc_cast.md:100-111`), and the recall scene is a contest with Ob lowered by a
`Reputation` tag. **Ledger for the record, contest for the confrontation, with a survivable escape** is
the correct shape, and the shape the whole ladder should copy.

---

## §5 — NERS verdicts

**The ladder core: not a rolling engine.** The 74 rungs, duty counts, vote tallies, Disposition
thresholds and capped suspicion accrual are a **deterministic ledger**. NERS does not apply; routed to
consistency/balance. The null result matters: **no dice have been bolted onto the ticks, so the classic
S-failure has not been committed here.** Keep it that way.

| # | site | verdict | note |
|---|---|---|---|
| 1 | **Rung-gate contests** — Burgher's Examination, Doctrinal Defense, Demotion Appeal, Recall scene, contested mastership | **N·R·S·E pass** | Legitimate rolling engines on the healthy d10 pool, legible Obs, graded degrees. **Leave alone.** Migrating to Mode B is the SKILL's own named over-correction (**N-inverse**): flattening a multi-exchange track to one probability destroys the surface the player reads. |
| 2 | **§6.4 officer-fate d10** — flat 1-4 wounded / 5-7 captured / 8-9 killed / 10 heroic (`faction_layer_v30.md:599-614`) | **R fail · S fail** | Not the classic S-failure — no ledger under it, nothing about the officer persists. **R-fail**: bare-stat table, no state coupling, no graded recoverability. **S-fail against its sibling**: the battle emitted a graded degree the table ignores. Remedy: **condition the row weights on battle degree and rout — a table refit, not Mode B.** Mode B here is **N-fail**: no odds are being weighed, it is a consequence roll. Correctly KEPT out of ED-874 scope (`faction_layer_v30.md:26`). |
| 3 | **`Faction.standing` written off dice degrees** | **not S-fail · R fail** | Rolls are the d10 pool vs a state-derived Ob — already legible-odds-with-stochastic-resolution. Defect is **R**: unbounded accumulator feeding the pool that writes it, at two entry points (`:81`, `:309`), no damper. Per §0.1 it is worse than unclamped — outside the descriptor roster, so there is no bound to apply. **Mode B is not the fix and would be the N-inverse.** |
| 4 | **Treaty lapse 0.90/arc, consent 0.28 flat** (`treaty.py:42-46,121-142`) | **S fail · E fail** | The textbook case: flat hazard draw, unconditioned on any state, on a pure ledger. E-fail because 0.90 teaches nothing. **Mode B is the named remedy** — lapse odds as a legible function of treaty age and relations. Two verified extras: the no-RNG fallback `roll = 0.95` **can never lapse at any canonical rate in 0.90–0.95**; and the module has **zero production callers.** Fix or delete; shipping as-is is worst. |
| 5 | **G606 / suspicion** | **structurally right; R fail pre-E11** | Capped deterministic accrual → threshold card → contest at the confrontation. The correct shape and the model for the rest. Defects are not dice defects: the **one-way ratchet** (R-fail, ruled fixed by E11, unauthored) and the **D6 advance-predicate fork**. |
| 6 | **§1.0d Performance Audit** | **N fail · S fail** | No dice — a second deterministic cascade on the same signal. N-fail now *provable*, not merely measured (§4). S-fail for two parallel demotion pathways off correlated triggers. Remedy is the D5 merge; no resolver change involved. |
| 7 | **`contest/faction.py::succession`** | **N·R·S·E pass, unreachable** | A multi-exchange Persuasion-Track bout whose track *is* the legible-odds surface; flattening to one Mode-B roll fails N and E together. Its problem is that nothing can call it. |
| 8 | **`mass_seizure.py:2-12`** — `P(declare)=((CI−60)/40)^3.3` | **pass** | Mode B already live in code. Named so nobody "fixes" it. |

**Over-correction sites, named:** rows 1, 2 (refit, don't convert) and 7; mass-battle resolution feeding
conquest (`faction_action.py:433-528`), already excluded from ED-874 for this reason; and
`crown_initiative`'s graded ±standing bands, a healthy stochastic engine on a bidirectional ledger.
**Five of eight sites want no Mode B at all.** The remedy applies at exactly one live site (treaty) and
at the treaty-shaped sites the ladder has not yet built.

---

## §6 — Cross-scale: tracing one officer, and where the trace breaks

An officer is the clearest cross-scale object the game could have: **one person, holding a post, that
governs a settlement, inside a faction, who may command in a battle** — all four scales, one object.
That is why its absence is diagnostic rather than merely incomplete.

**Trace: Bailiff Konrad Ems (NPC-G06)**, Crown levy agent at Goldenfurt, the corpus's own "suspicion
track made flesh" (`npc_cast.md:29`).

| scale | should exist | does exist | matrix cell |
|---|---|---|---|
| **Personal** | a person with convictions, ambition clock, leverage, Knots | a full prose dossier (`npc_cast.md:100-111`) and **no runtime object**; absent from `npc_registry.yaml` despite its own enforcement line; `generate_npc` builds anonymous NPCs and has no production call site | **S→P EMPTY** |
| **Settlement** | Goldenfurt sees its bailiff; suspicion moves when he logs a defiance | S-006 exists in the executing registry; `npc_ids` empty, `governor_id` `None` on all 37, and `Settlement.suspicion` (`registry.py:78`) has **zero writers** — grep returns only decl + serialize + deserialize | **S→P EMPTY** |
| **Faction** | Crown holds him with a rank on §1.1b | the executing Crown is `Faction(L,Sta,W,I,Mil,intel,standing)` with no members. His rank is undefined *in prose too*: §1.1b is the deliberately flat surface — **the ED-FA-0018 hole is exactly where Konrad's career would live** | **F→P BROKEN** |
| **Unit / battle** | the levy he raises is commanded by somebody | `_faction_to_unit` builds a Unit from `power = max(1,int(round(faction.Mil)))` with **`command=4` hardcoded** and every other field an inherited default carrying its own `[GAP: no canonical spec]` (`massbattle.py:63-90`). No commander slot; `officer_deaths` has zero `.py` hits | **F→U EXECUTED (lossy)** |

**Where the trace breaks: everywhere at once, for one reason.** Every crossing that executes carries a
scalar; every crossing that would carry a person does not exist. `_faction_to_unit` passes `Mil`; the
combat bridge passes `history = max(1, round(f.Mil))`; the council echo passes a stat name and a degree
back to the faction it came from. **A scalar is all you can pass when there is no object at the far
end** — which is why the officer is not one more feature but the removal of a blocker four systems
share.

The near-miss is instructive. `_emergency_council_parties` is a live **P→F** crossing
(EXECUTED-degenerate) firing ~975 times per batch, degenerate for exactly the reason the trace fails.
Meanwhile **F→P** is BROKEN in a way that names the same cause aloud: `combat_bridge.derive_parties`
works and returns `None` rather than fabricating an actor, is gated behind `DISPATCH_COMBAT_BRIDGE`
default-OFF, and is unreachable even when ON because no `queue_scene("combat", …)` call site exists.

One P5 constraint binds future work here (Chapter 5's catalogue — I cite, not re-derive): when U→P is
built, **the mass-battle resolver must call into `combat_engine_v1` for flagged encounters, never
maintain a second cheaper approximation** — building it otherwise commits Total War's two-decade
autoresolve divergence deliberately. And **never let the bridge's default be "off equals doesn't
exist"**; no surveyed precedent defends a flag that silently returns to zero-state.

---

## §7 — Historical precedent: what is banked, where there is none

Five officer-surface items were grounded in the 2026-07-09 comparative-governance pass and authored into
canon. All five are prose; none executes.

| ED | source | mechanism | status |
|---|---|---|---|
| **ED-FA-0019** | Kamakura *honryoando* vs *shin'on*, post-1274/81 reward crisis | **Recognition Fork** at every Std-3/5 Recognition Event: *Confirm* (ceremony fires, unlock withheld, demotion thresholds ease one step for a year-arc) vs *New-Grant* | `faction_politics_v30.md:98-112`; **PROPOSED**, REFINE-THEN-RATIFY — granter's decision rule and orphaned-New-Grant fate undefined |
| **ED-FA-0020** | *Sankin-kōtai* 1635 + hostage kin at Edo | **Court Attendance**: skipping doubles suspicion accrual; hostage-kin eases §1.0a one step but auto-escalates on a skip | `:115-125`; **RATIFIED**, prose only |
| **ED-FA-0021** | Zhang Juzheng's 1573 *kaochengfa* triplicate ledgers; unwound within months of his 1582 death | **§1.0d Performance Audit**, patron-death lapse as its own historical lapse condition | `:129-143`; **PROPOSED → ruled to MERGE (§4)**, unauthored |
| **ED-FA-0022** | Arte della Lana — capital, not craft, as the admission bar | Capital-gated Free Mastership + `Upstart` tag; Disposition −2, no apprentices 4 seasons | §2.5a; **RATIFIED**, prose only |
| **ED-FA-0023** | Book of the Eparch (Leo VI, c. 895–912) — five freeman guarantors, jointly liable | **Guarantor-gated guild entry**: 3–5 joint-liability sponsors, `Vouched-For` tags, guarantor burn-out lockout | §2.5a; **RATIFIED**, prose only |

**ED-FA-0021's grounding contains the argument for its own retirement.** The *kaochengfa* did not fail
from bad tuning; it unwound because its patron died. Its designed lapse condition is patron durability —
and §4 shows that *as a demotion channel* it is structurally redundant with G606. Honest disposition:
**merge the demotion cascade into the suspicion spine, and keep the patron-lapse structure as what it
actually models** — a bet on a patron's survival, i.e. an *internal-competition* primitive (§3.4 item 3),
not a second recall path. Preserves the history, deletes the duplication.

**ED-FA-0018 is the open top item, and it sits exactly where the officer object is thinnest.** Verified
at `registers/editorial_ledger_fa.jsonl:18` — `"status": "open"`, `"needs_jordan": true`, 2026-07-09:
*"Imperial Examination Ladder — Non-Skyrim-Eight credentialing pipeline; capped pass rates; direct Std-3
appointment; Waiting Laureate Pool… NEEDS_JORDAN fork: Does the deliberately-flat Crown Administrative
branch (§1.1b) get a differentiated, non-Skyrim-Eight sub-structure at all? (Highest-value rank fork;
recommended yes.)"*

I applied CLAUDE.md §0's five tests before treating it as live. It **survives all five**: no later ruling
touches it; the subject is live; no design document decides it (§1.1b's flatness is asserted, not
argued); no in-tree precedent settles it — the four branches that *do* have ladders were grounded from
Skyrim, which is what CHN-2 was proposed to correct; and the architecture is indifferent, since flat and
credentialed are both implementable. **Two defensible options lead to materially different games** — a
Crown bureaucracy you *join by examination* is a different political fiction from one you join by
patronage. That is a real escalation. Keep it flagged; answer it.

L5 §G adds a sibling precedent worth putting on the same fork: the **Florentine scrutiny-and-lot**
pipeline (*squittinio* → *imborsazione* → *tratta*, institutionalised 1328) as "a guard against faction
and patronage," **with its documented capture failure** — the Medici *accoppiatori* turning an impartial
lot into a weighted one. That pairing, a mechanism plus the attested way it was subverted, is a better
shape for Valoria than the examination pipeline alone, because **the subversion is the intra-faction
game**. Both sources are deleted from `main`; `grep sortition systems/` returns zero. [UNVERIFIED — I
take L5's quotation, not the archived corpus.]

**Officer surfaces with no historical grounding at all** (L7 §E's list; I spot-checked the first three
against the tables). The three that matter: **(1) the four primary ladder tables themselves** — grounded
in Skyrim guild progression, stated as such at `faction_politics_v30.md:6`, with the 2026-07-09 pass
having grounded only the cross-rank riders; **(2) §1.0a Demotion Magnitude** — a 2026-04-25 stress test,
no precedent, and the surface P1 §B1's arithmetic warning bears on most directly; **(3) Rival Cohort and
the pre-emption challenge** (`:53`) — ungrounded, and the *named* intra-faction rivalry mechanic. Then
seven more: Ministry Competence-Corruption tracks, rank = secession blast-radius, caste circumvention,
Deniability Debt / Shadow Renown, the Warden and Niflhel ladders, §6.4's fate table, E11's decay curve.
**Items 1–3 are the ladder's spine, its down-magnitudes and its only rivalry mechanic — load-bearing on
all three of Jordan's questions at once.**

---

## §8 — Recommendations

Ordered so the first two do not depend on Chapter 1's loader.

### §8.1 Decide what `Faction.standing` is — `engine/autoload/game_state.py` + `references/descriptor_registry.yaml`

An unbounded accumulator feeds a dice pool at two sites and is written by that pool's outcome; it is
outside the descriptor roster, which is why every write is a bare `+=`.

- **(a) Promote it.** Add a `fac.standing` row to `descriptor_registry.yaml` with floor and ceiling, add
  `'standing'` to `MULTS`, add the mapping in `engine/substrate/descriptors.py::_FIELD_TO_KEY`, and
  convert the ten bare writes to `adjust('standing', …)`.
- **(b) Demote it.** Remove `crown.standing` from the two pool expressions (`crown_initiative.py:81,309`)
  and keep it as a pure record. The feedback loop disappears; no range needs ratifying.

**Recommend (a)**, on §0's architecture test: the tree already decided this shape — six faction stats,
all registry-clamped since 2026-08-23 — and a seventh durable per-faction number outside that system is
the anomaly. **Do not pick 0–5, 0–7 or 0–10 by analogy**; those are three mechanisms' ranges and copying
one repeats the §0 error. Choose from what the writes do (±1/±2 across ten sites), which argues a small
symmetric band.

**Cost.** (a) **will move the seeded goldens** — `standing` enters a pool size, so clamping changes
draws, and `test_f7_smoke_oracle.py` and `test_mc_v18_regression.py` must be re-pinned in the same
commit. CLAUDE.md §7 flags golden re-pinning as an uncontrolled path, so it must be argued with a
before/after, not performed quietly. (b) may be golden-inert if standing is 0 at all reachable seeds —
**measurable before deciding, and measuring it is the first task.**

### §8.2 Give the emergency council two identities — `engine/cross_scale/scene_dispatch.py::_emergency_council_parties`

One function, roughly ten lines. Return two dicts instead of two ints, via the adapter path
`wrapper.py::_as_contestant` already supports:

```python
return ({"faculty": max(1, round(f.L)),         "standing_start": <seated rank>,     "evidence": [...]},
        {"faculty": max(1, round(7.0 - f.Sta)), "standing_start": <challenger rank>, "evidence": [...]})
```

**Highest-leverage small change in the chapter.** It converts the game's only live personal→faction
crossing from "a faction arguing with itself" into "two positions with different standing and different
evidence," on a **default-ON path firing ~975 times per golden batch**. No new mechanism, no new Key, no
ruling. And it opens §3.3's socket: when Chapter 1's loader lands, `standing_start` is where an
officer's rank goes, and `split_standing`'s `rank` (`resolver.py:204`) is the purpose-built non-ethos
channel for it.

Two sub-steps, in order: differentiate the **policies** first (both run `logos_spammer`, which the module
notes makes every verdict deterministically Memory-genre — arguably a bug fix, nearly free), then the
**starting standing** (the design change).

**Cost.** Both move the contest outcome distribution, so `GOLDEN_SCENES_RESOLVED`, `GOLDEN_WIN_SHARE` and
`GOLDEN_WINNERS` must be re-pinned with an argument. Honest caveat: until the loader lands the two sides
are *positions*, not *people* — this makes the contest non-degenerate, not populated.

### §8.3 Write one tag, at the one site that already exists — `registry.py::succeed_governor` + `parliamentary_action.py::propose_censure`

Valoria's demotion consequence-memory is fully built and completely unwritten: `ledger_sweep` guarantees
durable tags survive succession (`ledger.py:69-75`), `succeed_governor` already calls it (`registry.py:207`),
`TAG_KINDS` already holds Grudge/Debt/Leverage (`ledger.py:30`) — and nothing writes a tag.

**The change.** At the one demotion that executes — `propose_censure`'s pass branch
(`parliamentary_action.py:154-158`, currently two stat deltas and nothing else) — also write a durable
`Grudge` keyed to the proposer. Then give `succeed_governor` its first caller.

**Why this tag.** It is the mechanism P1 §A1 names as the fix for Dwarf Fortress's consequence-free
demotion, and the state §3.4 item 4 requires for divergence to be actable. **One write turns three inert
systems on at once**: the ledger gets its first producer, the demoted state gets a residual, and a future
divergence read gets something to read.

**Cost, in two parts.** The **tag write** is golden-inert (a list entry nothing consumes cannot move a
draw) — but that inertness is the catch: **a tag nobody reads is the unwritten writer's mirror image**,
and shipping it without a consumer is exactly the T-01 pattern this analysis diagnoses. It must land with
at least one read; the cheapest honest one is already designed — **the recall/censure contest's Ob lowered
by a `Reputation` tag and raised by a `Grudge`** — one term in one obstacle calculation, which is
Chapter 3's substrate and must be coordinated with its owner.

The **caller** is the expensive half. Giving `succeed_governor` a caller means there are governors, which
means persons in `world.npcs`, which per Chapter 1's controlled experiment **moves the seeded goldens** —
seed-42's winner shifted from Crown to Hafenmark on a two-NPC load, through `simulate_npc_actions`' draws
on `world.rng` (`systems/overview/sim/accounting.py:139`). **The prerequisite is an RNG substream for
season NPC drift, and it must land first**, or the officer layer's first commit is also an unargued
golden re-record. Sequence: **substream → loader → caller.** Not the other way round.

**Named but deliberately not recommended yet:** re-pointing the censure pipeline from factions to seats;
the `benefit-when-faction-loses` bloc flag; the §6.4 fate-table refit conditioned on battle degree; and
the D5 merge with its E11 co-requisite. The last is *ruled* and is the largest authored-but-unexecuted
item on this surface — excluded above only because §4 shows it is a design-authoring task needing D6
decided first, not a wiring task.

---

## §9 — Falsifier, stated and run

**Falsifier.** *If any executing code fills, promotes, demotes, recalls or censures a named officeholder
— or if any decision reads `hidden_allegiance`, `affiliation_loyalty` or a ledger Grudge/Debt/Leverage to
select an action against the actor's own faction — this chapter's core claim fails.*

**Run at `571ae14`:**

| probe | `.py` hits | disposition |
|---|---|---|
| `succeed_governor` | 2 | definition + its module's header list. **Zero callers.** |
| `governor_id` | 5 | decl, `to_dict`, `from_dict`, the uncalled assignment, one docstring. **Zero live setters.** |
| `hidden_allegiance` | 4 | decl, serialize, deserialize, the dropped write at `npe.py:327`. **Zero reads.** |
| `affiliation_loyalty` | 4 | same shape. **Zero reads by any decision.** |
| `add_tag` / `ledger_add` | 1 / 4 | owner modules only. **Zero external writers.** |
| `standing_change`, `officer_deaths`, `power_base`, `patron_id` | **0** | declared in prose registries; absent from code entirely. |
| `npc_registry` | 1 | a parse test. **No runtime loader.** |
| `coup_attempted` | 2 | `articulation.py:118` (a *consumer*) + one test. **No emitter.** |

**The falsifier does not fire.** Nearest miss: `contest/faction.py::succession`, exercised only by
`_kernel_tests.py:179`.

**Second artifact.** `python tools/m1_acceptance.py --summary` → verdict **NOT MET**; rows 1 and 4 FAIL,
row 3 PARTIAL, row 5 BLOCKED. Row 4 reports **0/7** and labels itself `⚠ DOC-DERIVED: counts state: done
in workplan_v6_progress.yaml, not execution`. Cited only as the milestone's honest self-report; no weight
placed on row 4, per §0.2.

### §9.1 A locator that did NOT check out — and it is one of this run's own

*(Caught by my own check of the working tree; the orchestrator independently issued the same correction
mid-run. Both readings agree. The duplication stands because this is the second time in this run that the
adversarial stage caught the orchestrator on a number.)*

The briefing instructed: *"Do not propagate the retracted ~87% win-share. The live golden is
`{Crown: 37.5, Church: 12.5, Hafenmark: 12.5, Varfell: 37.5}`."* **The live golden is not that.** At
`engine/tests/test_f7_smoke_oracle.py:267`:

```python
GOLDEN_WIN_SHARE = {'Crown': 62.5, 'Church': 25.0, 'Hafenmark': 0.0, 'Varfell': 12.5}
GOLDEN_WINNERS   = {'Crown': 5, 'Church': 2, 'Varfell': 1}
```

The `{37.5, 12.5, 12.5, 37.5}` figure appears at `:16` — inside the module **docstring**, prose narrating
what the file once pinned — and at `:75`, in a comment block explicitly labelled a *previous* pin. The
constant was regenerated 2026-08-24 when the mass-battle engine was swapped; the docstring was not.

**A §0.05 worked example, and the file warns about itself.** `:258-265`: both "PREVIOUS" blocks were
fabricated until 2026-08-23 because each re-record copied live values into the historical line — *"A
golden test pins the LIVE constants; nothing pins the prose, so a fabricated history stays green forever
and the next re-recorder reasons from it."* That is what happened one layer out: a run correcting one
stale number reached for the file's prose rather than its constant and propagated a second.

**For the record:** `~87%` remains retracted. The **live** golden at `571ae14` is
`{Crown: 62.5, Church: 25.0, Hafenmark: 0.0, Varfell: 12.5}`, `GOLDEN_SCENES_RESOLVED = 975`,
`GOLDEN_BATTLES_MEAN = 35.1`. And the file's own caveat covers all of them: n=8 at one seed **cannot
distinguish a balance change from noise**, and `:8` still demands an n ≥ 100 oracle that does not exist.
**None of these is a balance fact.** They are reproducibility pins.

---

## §10 — What I did not cover

- **The person loader** — Chapter 1's, cited as a hard dependency, deliberately not designed or costed
  here beyond inheriting its measured golden cost. **VSG's generator algorithm and calibration** —
  Chapter 4's; I use L4 §D.1's F9/F10/F11 *design content* (bloc, officer roster, patronage edges, the
  `benefit-when-faction-loses` flag) because the map assigns that content to me, and touch neither the
  sampler nor its weights. **The dice/degree/obstacle substrate** — Chapter 3's; I name `degree_from_net`
  (`engine/autoload/dice_engine.py:104`, verified as the single-owner margin ladder) only as the sibling
  §6.4's table fails to be smooth with. **The precedent failure catalogue** — Chapter 5's; I cite P5's
  autoresolve-divergence and default-off warnings in §6 rather than re-deriving them.
- **I did not re-run the PR#127 harness** — absent from the live tree and the recovered archive
  (searched). The 100% figure is quoted; §4's dominance argument is my own derivation, marked `[INFERRED]`.
- **I did not read** `faction_politics_v30.md` line-by-line beyond §1.0–§1.4, the ladder tables, §2.5a and
  the propagation table; Part 3 (caste), Part 6 (Baralta) and Part 7 (Ministries) I know only through L7.
  I did not open the archived `40_roster_officer_system.md`, `faction_succession_split_v30.md`,
  `npc_relational_graph_v30.md`, `faction_behavior_v30.md §3.2`, or
  `research/rise_to_power_roster_system_research_v1.md`.
- **I did not recount L7's ≥15 cross-cutting demotion mechanisms** (I verified seven individually and take
  the rest). I did recount the 74 rungs independently; they reproduce exactly.
- **I did not verify** whether `references/name_collision_database.yaml` lists the Hedda Vorn / Hedda
  Kronvald collision, nor L7's eleven vocabulary collisions beyond Standing, Governor and Suspicion.
- **I ran no campaign.** All "executes / does not" claims rest on module reads and greps at `571ae14`,
  plus the two execution artifacts in §9. Where L7 or L2 measured something I did not re-measure, I say
  whose measurement it is.
