# Faction Attributes — NERS + Historical-Value Audit (per attribute)
**Audit deliverable · 2026-06-09 · (1) NERS per attribute + interdependencies; (2) historical-precedent value, keep/expand/fold/cut**

Radically neutral: adding and subtracting are equally fine; only the quality of contribution counts. Grounded bottom-up
in the 2026-06-09 flatten + io-flatten + architecture review, and top-down in the repo's precedent research —
`faction_stats_renaissance_review.md` (per-stat Renaissance analogue + load-bearing verdict; the doc that argued Intel
back in), `2026-05-16-faction-ners-all-directions.md` (four turns of historical research → 10 throughlines, N-PASS), and
`ners_verdict_faction.md` (resolution-diagnostic F1–F9). NERS per `definitions.yaml` (N/R/S/E). No conversation search
needed — the precedent is in-repo.

---

## 0 — Verdict table (first)

| Attribute | N | R | S | E | Historical contribution | Verdict | What's needed |
|---|:--:|:--:|:--:|:--:|---|---|---|
| **Mandate** | ✅ | ◐→✅ | ✗→✅ | ◐→✅ | **strong** — legitimacy: papal bulls, investiture, dynastic claims (T-2) | **KEEP** (as derived readout) | the inversion (it's already its own precedent) |
| **Influence** | ✅ | ✅ | ◐ | ◐ | **strong** — Medici patronage, soft power (T-1) | **KEEP** | fix CI/Influence naming overload; define national basis |
| **Wealth** | ✅ | ✅ | ✗→✅ | ✅ | **strong** — Medici banking, trade revenue | **KEEP** | inversion (= settlement economy); kill Treasury double-source |
| **Military** | ✅ | ✅ | ✅ | ✅ | **strong** — standing armies, fortifications (T-2) | **KEEP** | inversion (= garrison aggregate); Wealth-coupling is good |
| **Intel** | ◐ | ✗ | ✗ | ◐ | **genuine** — Venice's Council of Ten, papal nuncios (T-8) — but mechanically thin | **KEEP + EXPAND** *or* **FOLD** | faction intel differentiation, counter-intel, info-asymmetry — **or** fold into Influence |
| **Stability** | ✅ | ◐ | ◐ | ◐ | **strong** — succession, coup resistance, Pazzi (T-2) | **KEEP** | differentiate the universal failure-sink (inversion does this); death-spiral already floored |

**Bottom line:** all six earn their place — each maps to a load-bearing Renaissance dynamic *and* carries a distinct
mechanical role, so **none is a clean cut.** The honest subtractions are not among the attributes: the **`§14` capitals
(Reputation/Treasury/Levies/Discipline) are vestigial and should be cut** (per the architecture review), **Intel is
under-included** (expand to its historical weight or fold it), and **Stability is over-loaded** as the catch-all failure
sink (trim by routing). The honest addition is Intel expansion *if* kept separate. The roster is sound; the work is the
S/E frictions — and the derived-stat inversion already resolves most of them.

---

## 1 — Mandate  *(in 70 / out 78; legitimacy)*

**Role + interdependencies.** The legitimacy axis. Derived (LPS-2e) from settlement L/PS (`faction_canon L214`); read by
Suppress / Censure / Outlawry / Excommunication / Royal Decree (d+σ) and as the parliamentary vote weight; written by 78
sites it shouldn't be (C-2). Couples downward to settlement L/PS and upward to vote power and (stale) Legitimacy capital.

**NERS.**
- **N — Pass.** Legitimacy is irreducible to wealth, force, or cohesion — a faction can be rich and armed yet illegitimate
  (the Restoration faction: PS climbs from 0, no Mandate). Distinct, load-bearing.
- **R — ◐→Pass.** *Was* fragile: `ners_verdict_faction` F1 flagged a bare-Mandate roll deciding pivotal, irreversible
  outcomes (the small-pool binary). d+σ's flat 0.10 leverage + treating Mandate as a derived aggregate remove the fragile
  bare roll. Robust **after** the inversion; not before.
- **S — Fail→Pass.** Today it is the *least* smooth attribute — C-1 (derivation arrow reversed vs `§14`) and C-2 (derived
  yet written 78×) are friction incarnate. The inversion (one direction: settlement → Mandate) is what makes it smooth.
- **E — ◐→Pass.** As "hold legitimate settlements → high Mandate" it is highly intuitable; as a base-stat-also-written it
  is opaque. Elegance is contingent on finishing the inversion.

**Historical value.** Strong. Renaissance legitimacy was the master variable — papal bulls, imperial investiture,
dynastic claims, constitutional authority (T-2: legitimacy and coercion co-constitutive). Not fantasy imposition.

**Verdict — KEEP, as the derived legitimacy readout.** No new systems needed; it is the best-served stat (Parliament,
Suppress, Excommunication, victory). Its only debt is the inversion it already half-completed.

---

## 2 — Influence  *(in 52 / out 23; diplomacy / soft power)*

**Role + interdependencies.** The diplomatic-reach axis and the single most-read resolution stat (Assert, Reconstitute,
Church Seizure, diplomacy). Couples to CI (Church Influence) — **and that coupling is a defect**: "Church Influence" is a
0–100 clock conflated with the 1–7 Influence stat, inflating its apparent writes.

**NERS.**
- **N — Pass.** Soft power / patronage is distinct from legitimacy and force (the Medici governed Florence for decades
  with little formal office, on Influence). T-1 (power is plural) requires it.
- **R — Pass.** Robust under d+σ; the dominant assertion lever across factions.
- **S — ◐.** The CI/Influence-stat naming overload is a real smoothness fault — two different quantities share a name, so
  reads/writes are ambiguous (the io-flatten had to disentangle them). Its derivation basis is national/diplomatic, not
  settlement — fine, but undefined.
- **E — ◐.** Intuitable as "diplomatic clout," but the CI overload makes the player (and the designer) unsure which
  "Influence" a rule means.

**Historical value.** Strong — Medici patronage networks, alliances, court politics. Load-bearing.

**Verdict — KEEP.** Two real fixes: (i) **resolve the CI vs Influence-stat naming overload** (rename the clock or the
stat); (ii) define its **national derivation basis** (alliances, parliamentary standing, recognition — not a settlement
sum). No expansion needed; it is already richly used.

---

## 3 — Wealth  *(in 17 / out 35; economy)*

**Role + interdependencies.** The economic axis; write-dominant (Trade, Embargo, Subsidy, stress). Feeds the spendable
Treasury and couples to Military (Wealth 0 → Military −1/season, unpaid mercenaries; FSS-LOOP-2 Wealth-restores-Military).

**NERS.**
- **N — Pass.** Economy is distinct and load-bearing; the Wealth→Military coupling is a *feature* (mercenary economies).
- **R — Pass.** Robust under d+σ (Trade, Economic Leverage). The Wealth-0 → Military drain is a bounded, intended pressure.
- **S — Fail→Pass.** C-3 (Treasury double-sourced: `Wealth×100` vs aggregated settlement Local Economy) is the friction;
  the inversion (Wealth = settlement Local-Economy aggregate, Treasury = that aggregate spent) resolves it cleanly.
- **E — Pass.** "Prosperous settlements → rich faction → spendable Treasury" is intuitable and emergent.

**Historical value.** Strong — Medici banking, trade revenue, mercenary funding. The economic engine of Renaissance power.

**Verdict — KEEP.** The inversion *strengthens* it (economy stops being a free-floating `×100` and becomes the sum of what
you actually hold). Kill the Treasury double-source. No new systems needed.

---

## 4 — Military  *(in 38 / out 17; coercive force)*

**Role + interdependencies.** The force axis; read-dominant (combat/siege pools, unit Power/Discipline ceilings, NPC
command rating). Feeds Levies (fielding cap). Couples to Wealth (above) and to the collapse loop (Stability → territory →
muster → Military).

**NERS.**
- **N — Pass.** Coercion is irreducible (T-2). Caps unit quality — a structural, distinct role.
- **R — Pass.** Robust — siege/battle pools, unit ceilings, command rating all consume it cleanly.
- **S — Pass.** Cleanly settlement-derivable (Σ Garrison Strength + holdings); the casualty writes route to garrisons.
  Scale-integrates well (faction Military → unit ceilings → mass battle).
- **E — Pass.** "Garrisoned, fortified settlements → strong army" is intuitable.

**Historical value.** Strong — standing armies, fortification networks, condottieri. Load-bearing.

**Verdict — KEEP.** The inversion (Military = garrison aggregate + casualty/muster events) strengthens it; the
Wealth↔Military coupling is good emergent design — retain. No expansion needed.

---

## 5 — Intel  *(in 10 / out 5; institutional intelligence) — the contested one*

**Role + interdependencies.** The smallest footprint of any attribute: a covert-ops resolution input (Investigate /
Counter-intelligence vs Ob 3; `M = Intel − 2` unique actions). Recently *split* from an Influence fallback
(`stats_1_7_scale L41`). No settlement basis; nearly no couplings.

**NERS.**
- **N — ◐.** Historically necessary (below) but mechanically marginal: it touches only covert ops, and was an Influence
  fallback until recently. Its *separateness* is the open question, not intelligence-as-a-concept.
- **R — Fail.** Underused — too few mechanics consume it to be "fully formed." A stat that decides only a handful of Ob-3
  covert rolls is not yet robust; there is no faction-level intel *differentiation* (the renaissance review's own
  complaint: "Investigate/Intel is flat Ob 2 for everyone").
- **S — Fail.** No settlement basis and almost no interdependencies — it floats. Under the inversion it has nothing to
  derive *from* unless an institutional basis is authored.
- **E — ◐.** Simple, but simplicity bought by under-use is not elegance — it is absence.

**Historical value — genuine, and stronger than its current mechanics.** Renaissance intelligence was *institutional*,
not personal: Venice's Council of Ten (the most sophisticated pre-modern apparatus), papal nuncios doubling as
intelligence officers, Machiavelli's Second Chancery. T-8 (information asymmetry is the substrate) is a real,
load-bearing dynamic. The repo deliberately restored Intel for exactly this reason — the history is sound; the *mechanics
have not caught up to the history*.

**Verdict — KEEP + EXPAND, or FOLD (dispassionate either way).**
- **Expand (if intelligence is to be a real axis):** add faction-level intel differentiation (Ob scales with attacker
  Intel vs defender Intel, not flat Ob 2/3); counter-intelligence and double-agent mechanics; *information asymmetry as a
  first-class system* (hidden enemy plans/positions revealed by Intel advantage) — which would also realize T-8, the one
  throughline currently under-mechanized. This is the single best "more robust inclusion" candidate in the roster.
- **Fold (if that expansion is not wanted):** a separate stat used only for covert-ops Ob is borderline-redundant with
  Influence; folding it back (Investigate pool = Influence) loses little *mechanically*. The cost is purely historical —
  it erases Venice's distinct intelligence edge.
- **The neutral call:** Intel is the one attribute whose keep-vs-cut turns on a design choice rather than on merit alone.
  Keep it only if you will mechanize T-8; otherwise fold it. Do not keep a thin separate stat for its own sake.

---

## 6 — Stability  *(in 49 / out 97; internal cohesion) — the over-loaded one*

**Role + interdependencies.** Internal cohesion — and the **universal failure sink**: nearly every Domain Action Failure
writes `Stability −1` (45 of its 97 outputs). Gates treaty terms (≥2 peace, ≤1 capitulation), drives the Accounting
Stability Check, and is the collapse trigger at 0. Sits at the center of the death-spiral loop (Stability → collapse →
territory loss → weaker muster → ...).

**NERS.**
- **N — Pass.** Cohesion is distinct and load-bearing (a unified poor faction outlasts a fractured rich one).
- **R — ◐.** `ners_verdict_faction` F3/F6 found a death-spiral (low Stability → collapse, irreversible). The FSS-LOOP-1
  deterministic floor (2026-05-30) bounds it. Robust *with* the floor; the floor must stay.
- **S — ◐.** The smoothness concern is **role-breadth**: Stability absorbs *every* action failure regardless of kind. A
  failed trade and a failed coup both cost "internal cohesion," which over-couples one variable to all of play (a soft
  Lesson-1 / one-variable-one-role pressure). Under the inversion this self-corrects: a failure perturbs the *relevant*
  settlement/national locus, which re-derives the *relevant* faction stat — a failed trade hits Prosperity→Wealth, not
  Stability.
- **E — ◐.** Intuitable as cohesion, but the catch-all sink makes "why did my Stability drop?" answerable only by "almost
  anything." Routing failures to their locus restores legibility.

**Historical value.** Strong — succession clarity, factional unity, coup resistance (the Pazzi conspiracy; T-2). Load-bearing.

**Verdict — KEEP.** Two notes, both already on the roadmap: keep the **FSS-LOOP floor** (it is what makes R pass); and let
the **inversion's locus-routing differentiate the failure sink** so cohesion stops being the universal consequence of
everything. No expansion; if anything, a controlled *narrowing* of its write surface.

---

## 7 — Cross-cutting (the radically-neutral net)

- **Subtract — the `§14` capitals.** Reputation/Treasury/Levies/Discipline are derived *from* faction stats — exactly the
  layer the architecture review found vestigial (built for the bare-stat-pool era, obsoleted by d+σ + the settlement
  substrate). Their genuine semantics re-home down (Treasury→settlement economy, Levies→garrison); the scalings retire.
  This is the clean cut, and it is what Jordan's "we may no longer need stats derived from faction statistics" named.
- **Add — Intel's missing systems (conditionally).** The one place "more robust inclusion" is warranted: information
  asymmetry (T-8) is historically central and currently under-mechanized. Either build it (and Intel earns its
  separateness) or fold Intel. No middle "keep it thin."
- **Narrow — Stability's failure-sink.** Not a cut, a re-route: failures hit their locus, not universally cohesion. The
  inversion delivers this for free.
- **Fix — two naming/derivation debts.** The CI vs Influence-stat overload, and the per-stat derivation bases (national
  for Influence/Intel; settlement for Mandate/Wealth/Military/Stability).

**The roster of six is historically and mechanically justified.** The defensible changes are not to *which* attributes
exist but to *how they are computed and coupled* — the derived-stat inversion — plus the single open design choice
(mechanize information asymmetry, or fold Intel). Every one of these is a quality judgment, not a preference: each maps to
a load-bearing dynamic or removes a redundancy, and each is Jordan-vetoable.

---
*Audit only. Grounded in `faction_stats_renaissance_review.md`, `2026-05-16-faction-ners-all-directions.md` (10
throughlines, N-PASS), `ners_verdict_faction.md` (F1–F9), the 2026-06-09 flatten / io-flatten / architecture review,
`definitions.yaml` (NERS). The Intel keep/expand/fold choice and the per-stat derivation bases are structural-ontology
calls reserved for Jordan.*
