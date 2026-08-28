# Game Precedent Companion — Part 3: Valoria Judged Against the Precedent

## Status: PROPOSED (2026-08-28) · reference under §0.05, not canon
## Version: v1.0 · Lane: IN (cross-cutting)
## Reads: `valoria_game_precedent_companion_v1{,_part2}.md`

**Reading order:** [Part 1 · Corpus and Survey](valoria_game_precedent_companion_v1.md) → [Part 2 · Comparison, Complements, Synergies](valoria_game_precedent_companion_v1_part2.md) → [Part 3 · The Critique](valoria_game_precedent_companion_v1_part3.md) → [Part 4 · Reconcile and Unify](valoria_game_precedent_companion_v1_part4.md)

Parts 1–2 report what other games built. This part turns that on Valoria: **each system judged against
the precedent for that same system.** Not "here is a feature list Valoria lacks" — the question is
what the genre treats as *table stakes* for a system of this kind, where Valoria sits relative to that
floor, and where it is ahead of the precedent and does not know it.

Three verdict classes are used, and the middle one is the interesting one:

- **BELOW THE FLOOR** — no surveyed title ships this system in this state, because the state is not
  playable.
- **AT THE FRONTIER** — Valoria is where the genre is, on a problem the genre has not solved. Not a
  deficiency; the correct place to be, and a warning against citing precedent for confidence.
- **AHEAD, AND UNAWARE** — Valoria has already built something the precedent's documented failures
  say is needed, and does not run it.

---

## §7.1 Faction strategy — BELOW THE FLOOR

**What the genre treats as table stakes: a faction has an interior that can disagree with itself.**
Victoria 3 composes government from interest groups holding clout, with the rest as opposition. CK3
makes vassal obligations negotiable contracts, and crown authority gates what the liege may *attempt*.
Old World emits a ruler's goals from his attitudes crossed with the influential families'. John
Company distributes office powers so that acting at all requires assembling a coalition. Kremlin holds
influence *over* politicians rather than owning them.

**Valoria:** four factions, six stats, one `rng.random()` draw per season against a re-weighted prior.
Two of the four have any branch at all; the other two fall through to a universal fallback, and
faction personality is `if faction.name == 'Crown'`. **Swap Hafenmark and Varfell's names in the
starting table and the campaign is unchanged.**

**The critique is not "add features."** It is that **no surveyed title models a faction as an
undifferentiated scalar bundle**, because a thing with no interior cannot have politics inside it.
Every mechanism the survey found interesting at this scale — contracts, blocs, coalitions, court
positions, ambitions — presupposes *parts*. Valoria's faction has none, so most of the genre's
faction-scale vocabulary is not merely unbuilt here; it is **untypeable**.

**What Valoria does that is genre-typical and should survive.** The action-selection signals are real
state reads — target-exists, military advantage, undergoverned share, proximate threat — not a bare
prior. That is more than several surveyed titles manage, and it is the skeleton an interior would hang
on rather than something to replace.

---

## §7.2 Parliament — BELOW THE FLOOR, and failing in the exact mirror of EU4

**Table stakes: procedure is the game; the vote is the formality.** The survey's whole finding at this
scale is that power is exercised in agenda control, speaking order, the chair's choice of which motion
to put, the veto and its record, and who drafts the response. Victoria 3 adds the one structural loan
the survey rates highest: **a law is a process with duration, running probability, discrete setbacks,
a failure state with cooldown, and an opposition that grows precisely because you attempted it.**

**Valoria:** every season, the lowest-Stability faction with territory and the highest-Legitimacy
other one are put on opposite sides of a motion with **no subject** — `motion_id = "parl_s7"` — and a
track moves. No chamber, no seats, no agenda, no order of business, no cost to propose, no scarcity of
sessions, and the only lever an uninvolved faction has is to be stable enough that its silence counts.

**The mirror is the sharp part.** EU4's estates are the canonical *ignorable* mechanic: legible,
well-motivated, and tuned so its failure state is never reached. Valoria's parliament has the opposite
symptom and **the same underlying defect** — it fires unconditionally every season and costs nothing.
Both are mechanisms whose firing rate is **decoupled from anything the player does**. EU4 is
decoupled at zero; Valoria is decoupled at one.

**Ahead, in one place, and worth defending.** The Persuasion Track is a *legible multi-exchange*
resolution — a visible track moving between stated thresholds. Victoria 3's enactment, for all its
structural superiority, is a hidden sequence of rolls the player watches as a percentage. **Do not
flatten the track to import the clock**; they operate at different time horizons (§8.3, R3).

---

## §7.3 Settlement governance — AHEAD, AND UNAWARE

**Table stakes: there aren't any, and that is the finding.** Total War added, removed and re-added the
governor role **three times for three different reasons across twenty years**. The survey's verdict is
explicit: *"There is no convergent answer — this is a real, unsettled design tension, not a solved
problem you are behind on."*

But the *components* are agreed, and one of them is a documented failure Valoria has already solved.
**Dwarf Fortress's counter-warning** is that demotion with no residual reads consequence-free once
survived — a comeback that resets to zero is a reset button. **CK3's landless track** is the opposite
pole: demotion must be its own game, not a debuff.

**Valoria's `succeed_governor` answers both, and predates the finding.** It does not merely swap a
string: it calls `ledger_sweep`, and durable tags (`ttl=None`) **survive the handover**, so a demoted
governor's record outlives him. `ledger_add` dedupes by `(kind, key)` and treats Reputation as a
single read of the officeholder. That is the residual DF lacks, built correctly, with **zero
callers** — and no tag writer of any kind exists anywhere in the tree.

**So the critique is not about the design.** It is that **a finished-and-parked system is
indistinguishable, from the player's seat, from an unbuilt one** — and the genre offers no example of
a governance layer shipping in that state, because nobody ships a layer nobody can reach. AP computes
to 2 everywhere and has no readers; L/PS are declared, serialised and touched by nothing but their own
serialiser; `facility_tier` drives the budget, the Weight table and the institutional ladder, and
**nothing sets it**, including the loader.

---

## §7.4 Territory and conquest — BELOW THE FLOOR, on the survey's own named error

**Table stakes: conquest is a negotiation, and a decree is a compliance roll.** Venice's *dedizione*
had subject cities keep their statutes, exemptions, guild privileges and councils in exchange for
loyalty and appellate supremacy. The survey generalises it: *what you leave standing determines what
governing costs for the rest of the game.* And it names the opposite pattern outright — **the decree
that produces an instant global state change is "the single most common error in governance games."**

**Valoria commits that error one level up.** Conquest transfers ownership immediately and the
designed three-season Occupation phase — with its per-season costs to both sides and its free
Resistance Check — is skipped entirely. The Entry Terms fork (Confirm Privileges / Impose
Administration) is the *dedizione* shape, is **the only authored rule anywhere that seeds settlement
Legitimacy**, and the code writes an `entry_terms_l_seed` that nothing reads.

**And a defect with no precedent parallel at all.** Turmoil, IP, PI and Strain are set at world
creation and never written again — four pressure gauges, all painted on. Turmoil is not merely
unused: it is **the third clause of the game's sole victory condition**, so `ps_ok` is unconditionally
true for the life of every campaign and GD-1 is materially one clause shorter than it reads. No
surveyed title ships a win condition with an inert clause, because in every surveyed title the win
condition is the thing that gets tested.

---

## §7.5 People — BELOW THE FLOOR, and built inside-out

**Table stakes: 5/5 lanes keep the threshold hidden and the inputs visible; 4/5 punish idleness; every
one of them has people.** In every seeded Valoria campaign, `world.npcs` is an empty dictionary.

**The sharper critique is structural rather than quantitative.** Every surveyed personnel system is
**primarily a relationship ledger with a roster attached** — JA2's pairwise matrix, TK's Satisfaction,
CK's opinion web, RoTK's loyalty. The roster is the index into the relationships; the relationships
are the mechanism.

Valoria has built it **inside-out**: identity is authored on 46/46 characters (role, faction,
convictions, source), capability on **1/46** — and that one records its `social` value as the string
`"3–4"` — and relationships on **0/46**. There is no Disposition field in code; its nearest runtime
relative is `affiliation_loyalty`, a different range under a different name, with **no mutator
anywhere**, so an NPC cannot change faction.

So the corpus has the half that is *content* and none of the half that is *mechanism*, which is why
the loader question keeps reading as easy and keeps not being. There is nothing to load the content
*into*.

**One thing Valoria does that the genre would recognise as correct:** `generate_npc` is a complete
two-tier generator — territory ecology, 60% bias toward the controlling faction, then a d6 deviation
flipping one axis so populations are not uniform. That is the shape CK's own fix converged on
(throttle the tap, bias the draw). It has no call site.

---

## §7.6 Economy — BELOW THE FLOOR, on a defect the genre has no name for

**Table stakes: 4/4 franchises separate the levy from the professional**, and every one of them
resolves non-payment somehow — Shogun 2 auto-culls, Medieval II requires manual disbanding, CK's
militia desert when upkeep lapses.

**Valoria has four Wealth write sites in the entire engine, all of them costs, and no income
anywhere.** No surveyed title has a resource with no source, so the survey supplies no failure mode
for this — there is nothing to compare it to. It is not a balance problem; it is an open circuit.

**And the levy/professional finding indicts Muster specifically rather than generally.** ED-FA-0009's
grounding is Wallenstein — a mercenary contractor paid regardless — which is *the professional model*.
So Valoria's single Muster is not an under-built levy; it is a correctly-grounded professional
recruitment action wearing a generic label, with the levy half absent and unnamed. That is a naming
and canon problem before it is a mechanics problem.

---

## §7.7 Mass battle — the engine is ABOVE the genre; the seam is BELOW it

**Table stakes at the seam: composition varies.** Total War varies unit rosters behind building
chains, Three Kingdoms gates types on commander class, Brigandine varies by knight, JA2 and Unicorn
Overlord vary by squad. **4/4 treat garrison as an assignment of the same pool**, never a cheaper
tier.

**Valoria's engine is genuinely strong** — troop types, equipment, formations, per-cell morale,
Lanchester signatures, stamina, encirclement — and its seam is one integer wide. `_faction_to_unit`
builds both armies from `power = max(1, round(faction.Mil))` with identical shape, tier, position
`(8,12)`, facing, command 4, discipline 5, morale 5.

**So every strategic battle is geometrically symmetric before it starts, and only one number differs.**
No surveyed title does this. `terrain` is a declared parameter that appears nowhere in the function
body and whose only caller passes `None`. `derive_command` exists, is clamped, and its flag now
defaults ON — and the adapter never sets either attribute, so the campaign path silently falls back to
the hardcoded 4.

**The critique in one sentence:** an engine that can express formation, equipment and per-cell morale,
fed one rounded integer, is the most expensive possible way to compute `power_a` versus `power_b`.

---

## §7.8 Cross-scale — AT THE FRONTIER, and sitting where its nearest rival sits

**Table stakes: nobody has solved this.** *"No precedent in this survey demonstrates a mechanism whose
personal-scale contribution is provably leverage-in-band from N=1 to N=1000+."* Every mechanism is
scale-blind (Dominions, TW's lord aura) or fully fused (Mount & Blade). Well-funded teams tried.

**So Valoria is at the frontier here, not behind it — and that is the uncomfortable part.** Its
cross-scale coupling is the thing its own doctrine names as the differentiator; `throughlines_meta_infill.md`
defines the Ω-clause *against* **Mount & Blade's faction politics versus character combat** as the
paradigm of mechanically isolated layers.

**Valoria currently sits where M&B sits.** One of eight handoffs is production-reachable. One of eight
mandatory zoom-in triggers is evaluable, and it fires an emergency council whose two sides are derived
from **the same faction's own aggregates** — a faction arguing with itself, which works precisely
because it needs nobody in the room. The combat bridge is default-OFF and has no producer even when
ON. And both leverage failure poles are live in the same sixteen lines: `pc_incapacitated` applies
flat regardless of battle size (the Dominions shape), while `contested_figure_wounded` is a flat
+0.15 Ob whose probability effect decays as `1/√N` (the Mount & Blade shape).

**Being unreachable is why nobody has had to decide.** When a producer lands, those two carriers
become the seam's semantics **by default — inherited rather than chosen.**

---

## §7.9 Resolution kernel — AHEAD on ownership, BEHIND on calibration

**Ahead:** one owner for the dice, one for the margin ladder, both guarded, and ED-IN-0196 closed the
TN question by making non-conformance **impossible** (`_require_tn7` raises) rather than merely
discouraged. No surveyed title governs its own resolver that way; this is the healthiest system in the
tree and the pattern every other single-owner claim should be held to.

**Behind, and it is the same audit Blades never ran.** At a fixed `Ob = 3`, failure collapses from
93% at pool 2 to 6% at pool 20 — Blades' curve with different arithmetic. Scaling the obstacle with
the opponent fixes the *failure*-band collapse but **the Partial band still falls monotonically,
0.320 → 0.093**, because the ladder's Partial window is a fixed width of exactly one success laid over
a distribution whose spread grows as √N. **No obstacle derivation cures that; only a band width that
scales with the pool.**

**And the over-correction to refuse**, since it is the standing temptation: do not answer this with a
compensating die, a second roll or a re-roll. One band definition parameterised on pool size, not more
apparatus.

---

## §7.10 Social contest — AT THE POINT BEFORE Burning Wheel's failure, which is the good place

Burning Wheel's *Duel of Wits* is the closest existing analogue and its documented collapse is the
survey's most valuable single finding: **players converge on the two highest-damage manoeuvres and
stop; Rebuttal goes unused because too much beats it.** A second, independent failure: at a 21-vs-11
Body of Argument it degenerates to "the bigger number wins fast."

**Valoria has the resolution chassis and has not authored the manoeuvre set** — which means it is
standing at the point *before* the documented failure, knowing what causes it. That is a genuinely
advantaged position and it converts a warning into a design constraint that can still be met:
manoeuvres must differ in **what they change about the state of the argument**, not in how much they
subtract.

**The null that bounds the ambition:** *no game in this survey models the content of an argument.* If
Valoria authors that, it is doing original work with no precedent to fall back on — which is a
legitimate thing to do and must be said plainly rather than implied.

---

## §7.11 The critique in aggregate

| System | Verdict | The one-line reason |
|---|---|---|
| Faction strategy | **Below the floor** | No surveyed title models a faction as a scalar bundle, because a thing with no interior cannot have politics inside it |
| Parliament | **Below the floor** | The arithmetic of a vote without the procedure of one — and procedure is where the survey locates the power |
| Settlement governance | **Ahead, unaware** | Its `ledger_sweep` solves DF's documented residual failure, and has zero callers |
| Territory / conquest | **Below the floor** | Commits the survey's named "single most common error", one level up — and ships an inert clause inside the sole win condition |
| People | **Below the floor, built inside-out** | Every surveyed system is a relationship ledger with a roster attached; Valoria has the roster and no relationships |
| Economy | **Below the floor** | No surveyed title has a resource with no source, so there is no failure mode to compare against |
| Mass battle — engine | **Above the genre** | Formation, equipment, per-cell morale, encirclement |
| Mass battle — seam | **Below the floor** | Both armies identical but for one integer; no surveyed title ships symmetric battles |
| Cross-scale | **At the frontier** | Nobody solved it — and Valoria currently sits where the game it defines itself against sits |
| Resolution kernel | **Ahead on ownership, behind on calibration** | Non-conformance made impossible; the Partial band still collapses 0.320 → 0.093 |
| Social contest | **At the point before the known failure** | The chassis exists, the manoeuvre set does not, and the collapse condition is documented |

**The pattern.** Six systems sit below a floor the genre established decades ago, and in **four of
those six the missing piece is a caller rather than a mechanic**. Two systems are genuinely at or past
the frontier — the kernel's self-governance and the battle engine — and both are throttled by a seam
below them. Nothing here is a case that Valoria is over-ambitious. It is a case that **the ambitious
parts are built and the ordinary parts are not.**
