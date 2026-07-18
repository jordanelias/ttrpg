# Valoria — Precedent → Mechanism Design Brief

**Status: SPECULATIVE ANALYSIS — proposals and suggestions. Not canon, not ratified design.**
The fourth in the 2026-07-17/18 narrative series (assessment → companion → cast-and-culture → **this**). Where the
assessment mapped *texture* and the companion proposed *mechanisms in prose*, this brief does the **translation
engineering**: it turns the precedent-and-texture corpus into concrete **actions, events, choices, and substrate**
with **declared I/O per mechanic**, sited in the real subsystems. It ratifies nothing and touches no ledger,
`CURRENT.md` row, or module contract.

**Disciplines this document obeys:**
- **Grounding is three-axis both/and** — every mechanic leads with a **real-actor / real-politics precedent**, keeps a
  **literary lens** where it adds form, and now names an **acclaimed-game precedent** (Jordan's third axis) for the
  interaction pattern. Each axis is load-bearing; none is decoration.
- **Declared I/O is PROPOSED, transcribed against the live vocabulary, and binds nothing.** Every `consumes`/`emits`
  block below uses the **real Key type families and resolvers** from `references/module_contracts.yaml`
  (`da.*` / `env.* `/ `scene.*` / `state.*` / `meta.*`; resolvers `d_sigma`, `dice_pool`,
  `deterministic_accounting`, `state_reader`, `manifest`, `clock_advance`) and the real clocks (**MS**/Mending
  Stability, **IP**/Institutional Pressure, **Turmoil**, **CI**/Church Influence, **Coherence**, `persuasion_track`,
  Mandate, `knot strain`, conviction scars). **Any new Key type I propose is tagged `[PROPOSED]`** and would need a
  `key_type_registry` allocation + a `module_contracts` edge before it is real.
- **Canon holds (P-01–P-15).** Rendering is consciousness performed (P-03); the barrier and the Forgetting are
  metaphysical, not institutional (P-08/P-13); the caste is Altonian colonial residue; monstrosity is ontological
  (P-07); Solmund is never resolved.
- **Naming follows the corpus** — no CI-blocked deprecated name; every new proper noun is a proposal pending
  `id_reservations.yaml` + the `placeholder_names` contamination audit.
- **Threads into the companion, does not duplicate it.** Where a mechanic instantiates a companion §3 idea (Attention
  §3.1, belief-as-rendering §3.2, Collision §3.3, Omelas compass §3.4, Buried Giant §3.5, Testament §3.6,
  reader-as-renderer §3.7, three-body ratchet §3.9), it is cited, not re-argued.

---
---

# PART I — THE TRANSLATION DISCIPLINE

## I.1 The one rule that makes a mechanic Valorian, not reskinned

The corpus's own cliché-guard is the design test: a mechanic earns its place only when it **binds a precedent to a
substrate truth that is ontologically real in Valoria and nowhere else.** A "toll-dispute quest" or a "faction
meter" fails the test — any setting could host them. Four substrate truths are the binding sites:

| Canon truth | What it makes mechanically possible |
|---|---|
| **P-01/P-03 — rendering *is* consciousness performed** | Observation and belief are *constitutive*, not epistemic. The attention/UI layer can be diegetic substrate; what is attended-to or believed becomes more real. |
| **P-08/P-13 — the barrier and the Forgetting are metaphysical** | Some knowledge cannot be *held*, by physics not secrecy. Knowledge-decay is a law, not a skill check to beat. |
| **The three-body ratchet** (companion §3.9) | Baralta/Vaynard/Almqvist *always* win; strain is monotone; the player chooses *what compounds*, never *whether*. |
| **Caste as Altonian colonial residue** | The foundational injustice is structural and inherited — a live moral-mechanical axis, not a sidequest. |

Every action/event/choice in this brief is a **precedent × one of those four**. The product is what a competitor
cannot copy, because copying it would mean importing Valoria's metaphysics.

## I.2 The two contests are two clock-sets (the spine of everything below)

The assessment's thesis — *"two simultaneous contests: who governs the peninsula AND whether it survives"* — is not
just theme. It is **two clock families already in the substrate**, and naming them is what lets a mechanic declare
which contest it serves:

- **The political contest ("who governs")** runs on **IP** (Institutional Pressure, 0–100, the Altonian invasion),
  **Turmoil** (0–10), faction **Mandate**, **CI** (Church Influence, 0–100), and the faction stats 1–7. These are
  *owned* clocks (`peninsular_strain`, `settlement_layer`, `territorial_piety`, `faction_state`).
- **The ontological contest ("whether it survives")** runs on **MS** (Mending Stability — the world substrate;
  −1/in-game-year baseline drift; MS=0 → Post-Calamity, MS≤5 sustained → Second Calamity terminal) and **Coherence**
  (the Threadwork practitioner's structural integrity). **MS is currently an *unowned* clock** — `victory` only
  *reads* it; no module in `module_contracts.yaml` emits to it. That gap is a design opportunity, not a defect to
  paper over (Part V).

**The three-body ratchet is the political-clock engine; the Forgetting / Regard / Threadwork nexus is the MS engine.**
The best mechanics couple them — a political win that costs MS is the whole game's tragedy in one action.

## I.3 The translation pipeline (maps onto the real Key contract)

A repeatable five-step method, so authoring is not ad hoc. It lands exactly on the `module_contracts` IN → resolver
→ OUT shape:

1. **Name the texture** — a specific pressure from the assessment (e.g. "Himlensendt wins by making you *reveal*").
2. **Assemble the precedent triad** — historical + literary + game, each load-bearing.
3. **Declare the substrate binding** — which existing Key types does it `consume`? which resolver? which clocks does
   it move? (Reuse real types; tag new ones `[PROPOSED]`.)
4. **Add the Valorian twist** — the ×-factor from I.1. *This is the step usually skipped, and it is the whole game.*
5. **Site and tier it** — subsystem home, declared `emits`, and Passive → Active promotion on recurrence.

---
---

# PART II — THE FIVE SIGNATURE SUBSTRATES

Author these five *once*; everything in Part III instantiates them. Each is the mechanization of a canon truth, is
cross-scale, and (where noted) **fills a real gap** in the current contract graph.

## II.1 ① REGARD — attention as a rendering act (P-03)

**Canon truth mechanized:** rendering *is* consciousness performed, so *what the player attends to becomes more real
and more resolvable*, and what is ignored stays in potentia. This is the one mechanic no other game can justify,
because only here is observation ontological rather than informational.

**Precedent triad:** phenomenology's *intentionality* (Husserl/Merleau-Ponty — attention constitutes its object) ×
the reader-completes-the-text (Calvino's *If on a winter's night*, Borges) — *this is companion §3.7, the one place
the literary lens is honestly primary* × **games:** *Outer Wilds* / *The Stanley Parable* (knowing changes the
world), and the "quality"-gated attention economy of *Fallen London*.

**Proposed declared I/O:**
```
NAME:      Regard (attention budget)
CONSUMES:  * from engine  (universal read of the Key stream, like articulation_layer)
RESOLVER:  state_reader + manifest  (a per-scene finite attention budget the player allocates)
EMITS:     [PROPOSED] meta.regarded {target, intensity}
CLOCKS:    feeds articulation_layer's significance function; a Regarded threat gains resolution
           (becomes an actionable Key); an un-Regarded latent threat cannot resolve against the player
TIER:      substrate (Active surface = the zoom-stack / player_agency attention allocation)
FILLS:     gives articulation_layer a player-driven input; a candidate *owner-side* feed for MS
           (deliberate Regard of the wound is how a Warden "tends" it — see II.3/III)
```
**Cross-scale:** Regard is scale-agnostic — attending to a duel, a parliamentary maneuver, or a settlement rite all
mint `meta.regarded`. It is the diegetic justification for the zoom-stack itself.

## II.2 ② THE RATCHET — designed so all three rivals always win (three-body)

**Canon truth mechanized:** the three-body ratchet (companion §3.9). Resolving a top-scale crisis *requires* granting
Baralta, Vaynard, and Almqvist each a structural gain; the resolution itself raises the floor of the next crisis.
Almud can only choose *which* catastrophe compounds.

**Precedent triad:** *tertius gaudens* (Simmel) as practiced by Metternich's congress system and Bismarck's
alliance-juggling — the broker who profits from every quarrel × the impossible-choice statesman (Mantel's Cromwell,
le Carré's Smiley — the superb operator with no *right* move) × **games:** *Crusader Kings* (you defer realm-collapse,
never solve it) and *Reigns* (every choice pays a cost to someone).

**Proposed declared I/O:**
```
NAME:      The Concession (a resolution modifier on Domain Actions / parliamentary contests)
CONSUMES:  scene.contest_resolved (from social_contest, a parliamentary vote),
           da.diplomatic_alliance / da.public_governance (from domain_actions)
RESOLVER:  d_sigma (domain_actions), consistent with ED-FA-0006 da.* outcome-tagging
EMITS:     [PROPOSED] da.concession {beneficiary ∈ {Hafenmark, Varfell, Crown-rival}, structural_gain}
           — an OUTCOME TAG per ED-FA-0006, not a new module
CLOCKS:    mints env.peninsular_strain_shock with strain_delta > 0 (MONOTONE — never negative);
           raises Turmoil and the *next* crisis's Ob floor; each beneficiary gains a permanent standing Key
TIER:      Active (the signature FA action)
TWIST:     there is no branch that satisfies all three and none that satisfies none — the resolver
           is constrained so every resolution distributes exactly the three gains (Almud's impossible choice)
```
**Cross-scale:** the ratchet is the same dynamic at four scales (Part IV) — a parliamentary contest (SC), a domain
concession (FA), a delaying battle vs Altonia (MB), a settlement temperament-drift (SE).

## II.3 ③ THE FORGETTING — knowledge as a decaying substrate (P-13)

**Canon truth mechanized:** the barrier is metaphysical (P-08) and the Forgetting is real (P-13). Near the wound,
findings erode from the player's *own* record; retention is gated by the character's Threadwork-Sensitivity (TS≥30).

**Precedent triad:** the Chernobyl liquidators who could not be told what they carried (Orm, the Warden) × Ishiguro's
*The Buried Giant* — a mist of forgetting that is *legislated*, not liftable (companion §3.5) × **games:**
*Pathologic* (a town where knowledge and supply decay under you) and *Sunless Sea* (Terror as an attritional clock).

**Proposed declared I/O:**
```
NAME:      Reading in the Forgetting (an investigation modifier in/near T15 and the maritime zone)
CONSUMES:  scene.investigation_resolved (fieldwork), env.peninsular_strain_shock
RESOLVER:  dice_pool (fieldwork_knots), but the Evidence Track runs BACKWARD in-zone
EMITS:     meta.knot_ruptured (findings lost), state.belief_revised
CLOCKS:    Evidence Track decays per season in-zone; retention GATED by TS≥30 (below that, notes self-redact);
           deep investigation can cost MS (rendering the wound harder by attending wrongly — couples to ①)
TIER:      Active (the signature FI mechanic; also the Warden-tending loop)
TWIST:     no skill defeats it — the player chooses *what to learn before it is lost*, not whether to lose it
```
**Cross-scale:** at personal scale this is a redacting notebook; at world scale it is the maritime Forgetting boundary
(Joren Bergvall's survey), mapped only by sustained Regard (①).

## II.4 ④ THE LEDGER-IS-REAL — witness and record as ontology (P-03/P-08)

**Canon truth mechanized:** belief-as-rendering (companion §3.2). A written or witnessed truth, once concentrated,
becomes substrate-true. The Roll of Burghers, the Löwenritter deed-ledger, the confession, the Testament (§3.6) are
not bookkeeping — they *render*.

**Precedent triad:** the Venetian *Serrata* and the muster-roll — enrollment that *constitutes* a right, not records
it × Borges' *Tlön, Uqbar, Orbis Tertius* — belief instantiates the world (the honest metaphysics behind §3.2) ×
**games:** *Pentiment* (what is written into the record becomes history) and *Kingdom Come: Deliverance* (reputation
as a witnessed, accreting fact).

**Proposed declared I/O:**
```
NAME:      The Witnessed Deed / the Enrollment (a cross-subsystem outcome primitive)
CONSUMES:  scene.witness (npc_behavior/scene_slate), scene.combat_resolved, scene.contest_resolved
RESOLVER:  deterministic_accounting (accrues to a ledger state), gated on witness presence
EMITS:     [PROPOSED] state.witnessed {deed, ledger, witnesses}; feeds state.standing_change
CLOCKS:    settlement Legitimacy / faction Mandate / Löwenritter standing move ONLY on a witnessed/enrolled deed;
           an un-enrolled person cannot own or testify (the Hafenmark caste mechanism, C.1)
TIER:      Active
TWIST:     the *unwitnessed* deed does not count and the *un-enrolled* person is not fully real to the system —
           the record is the rendering, so gatekeepers of records (Griseldis Amtmann, B.3) hold ontological power
```
**Cross-scale:** a combat deed (PC), a parliamentary act on the record (FA/SC), a settlement enrollment (SE), a
Testament persisting a character (WR) are the same primitive at four scales.

## II.5 ⑤ THE COMPASS — the caste as a live mechanical axis

**Canon truth mechanized:** the Omelas compass (companion §3.4), repaired to include the Southern Einhir as
*subjects* with their own stances (endure/transmit, assimilate, reclaim-unknowing, revolt).

**Precedent triad:** the Stellinga revolt and the *converso* assimilation — the marginalized acting for themselves,
not being acted upon × Le Guin's *The Ones Who Walk Away from Omelas* — the foundational injustice as an unavoidable
moral fact × **games:** *Disco Elysium* and *Tyranny* — a political-vision axis that colors every check.

**Proposed declared I/O:**
```
NAME:      The Compass (a stance axis read across choices)
CONSUMES:  * from engine (articulation_layer already reads the full stream)
RESOLVER:  state_reader (a significance-function read; the armature dot-product of substrate §2.5)
EMITS:     [PROPOSED] state.stance_registered {actor, pole ∈ {endure, assimilate, reclaim, revolt, complicit}}
CLOCKS:    modifies faction Mandate legitimacy and npc_behavior opinion drift; a choice's Compass pole
           is logged and compounds (the Penitent's Gambit spends it — III, FA)
TIER:      substrate (Active surface = a per-choice framing, not a meter)
TWIST:     the injustice is colonial residue, so the axis is *structural and inescapable* — there is no "resolve
           the caste" ending, only stances taken and their accreting cost
```

---
---

# PART III — THE SUBSYSTEM MATRIX (concrete actions / events / choices)

Each entry: the texture, the precedent triad (H = historical, L = literary, G = game), the Valorian twist, the
**proposed declared I/O in real vocabulary**, tier, and which signature substrate(s) it rides.

## III.1 Factions (FA) — the ratchet made an action set

**"The Concession"** *(the signature ratchet action).* H: Metternich/Bismarck *tertius gaudens* · L: le Carré's
Smiley · G: *Crusader Kings* defer-collapse. **Twist:** every resolution distributes exactly three structural gains
and raises the next floor. **I/O:** `consumes scene.contest_resolved, da.public_governance` → `d_sigma` →
`emits [PROPOSED] da.concession + env.peninsular_strain_shock(strain_delta>0)`; moves **Turmoil ↑**, mints permanent
standing Keys. **Tier:** Active. **Rides:** ②.

**"The Penitent's Gambit"** *(spend moral standing for position; from `arcs_10_18`).* H: the Investiture Controversy
walk to Canossa · L: the humiliation-as-strategy of a Mantel court scene · G: *Crusader Kings* stress/dread trades.
**Twist:** resolves a §3.3 **Collision** (two *legitimate* authorities, one jurisdiction) Concordat-of-Worms style —
both get a face-saving partial — while spending a **Compass** pole. **I/O:** `consumes da.antinomian_action,
state.stance_registered` → `d_sigma` → `emits state.standing_change, state.succession`; moves **Mandate**,
**CI**. **Tier:** Active. **Rides:** ⑤ + the Collision class.

**"The Aloof Edit"** *(Vaynard's signature — win by controlling the record).* H: chancery/archival control (the
medieval *cursus* and forged charters) · L: the archivist-villain · G: *Pentiment*'s record-as-truth. **Twist:**
alters the Roll/record so a past act reads differently — **④ makes the edit ontologically real**, not a lie. **I/O:**
`consumes state.witnessed` → `deterministic_accounting` → `emits [PROPOSED] state.record_amended`; moves **Mandate**
legitimacy retroactively. **Tier:** Active. **Rides:** ④.

## III.2 Social Contest (SC) — the contest you lose by revealing

**"The Examination"** *(Himlensendt/Haelgrund win by extraction, not defeat).* H: the Bellarmine-style
inquisitorial examination · L: Porfiry Petrovich in *Crime and Punishment* · G: *Disco Elysium* checks made against
your own psyche. **Twist:** the stake is a *truth*, and a revealed truth (P-08) can render into the substrate — some
things, once said, cannot be unsaid. **I/O:** `consumes scene.dialogue, state.opinion_revised` → `dice_pool`
(social_contest) → `emits scene.contest_resolved + [PROPOSED] meta.revelation_rendered`; moves `persuasion_track`,
and on a forced high-stakes reveal, **MS −1** (a rendered truth reshapes the world). **Tier:** Active. **Rides:**
④ + ①.

**"The Belief Cascade"** *(a contest that shifts what is true, not just what is thought; companion §3.2).* H: the
self-fulfilling bank-run / legitimacy cascade · L: Borges' *Tlön* · G: *Fallen London* quality-gated belief. **Twist:**
when enough NPC belief concentrates on a proposition, articulation promotes it from opinion to substrate fact
(P-03). **I/O:** `consumes state.opinion_revised (×N over threshold)` → `state_reader` (articulation) →
`emits [PROPOSED] state.belief_rendered`; can move **CI** or **MS**. **Tier:** Active. **Rides:** ④.

## III.3 Fieldwork / Investigation (FI) — clues the source cannot read

**"Reading the Weave"** *(the clue is a craft-song its bearer cannot know is meaningful; Aslaug, B.2).* H:
Baltic/Irish revival craft that carried suppressed technique · L: the unwitting-vessel motif · G: *Return of the
Obra Dinn* / *Outer Wilds* (assembling a truth the world's inhabitants can't). **Twist:** P-08 means the *source*
literally cannot perceive the substrate-heritage in her own weaving; only a TS-sensitive investigator can. **I/O:**
`consumes scene.investigation_resolved` → `dice_pool` → `emits meta.knot_formed, state.belief_revised`; gated on
investigator **TS**. **Tier:** Active. **Rides:** ③ + ⑤.

**"The Redacting Notebook"** *(investigation near the wound; II.3 instantiated).* H: Chernobyl liquidators · L:
*The Buried Giant* · G: *Pathologic* decay. **Twist:** the Evidence Track runs backward in-zone. **I/O:**
`consumes env.peninsular_strain_shock` → `dice_pool` → `emits meta.knot_ruptured`; **Evidence Track ↓**, TS≥30
retention gate, optional **MS** cost. **Tier:** Active. **Rides:** ③ + ①.

## III.4 Combat (PC) — honor accounted, conviction-branched

**"The Witnessed Deed"** *(combat only mints standing if seen; II.4 instantiated).* H: the chivalric muster-roll ·
L: Malory's accounted honor · G: *Kingdom Come: Deliverance* reputation. **Twist:** an unwitnessed victory feeds no
faction. **I/O:** `personal_combat emits scene.combat_resolved` → `consumes scene.witness` →
`deterministic_accounting` → `emits [PROPOSED] state.witnessed`; moves Löwenritter standing / **Mandate** via Domain
Echo (`scale_transitions §3.4`). **Tier:** Active. **Rides:** ④.

**"Conviction Stance"** *(who you are branches how you fight).* H: confessional/martial cultures where creed shaped
technique · L: the fighting-style-as-character trope done seriously · G: *Sekiro*/*For Honor* stance systems, but
tied to belief not button. **Twist:** the `d_sigma` advantage (μ-shift on the roll) is modulated by the combatant's
top **Conviction** and exposed **Resonant Style** (from the conviction/scar track). **I/O:** `consumes
scene.combat_strike` → `d_sigma` → `emits scene.combat_hit`; reads conviction scars, can `emit state.scar_acquired`
under a crisis. **Tier:** Active (a resolver modifier, not a new module). **Rides:** — (personal-scale, but feeds ④).

## III.5 Mass Battle (MB) — the enemy is a weather system

**"The Delaying Action"** *(you never beat Altonia, you buy clock; Bryennios/Kaltenbach, B.1).* H: Byzantine *thema*
reconquest and the Roman *limes* in decline · L: Coetzee's *Waiting for the Barbarians* (empire as climate) · G:
*Into the Breach* (survive-not-win) and *Old World* attrition. **Twist:** a won battle does not remove IP — it
*slows the IP clock*, and Kaltenbach's claim frames the invader as a *restorer* (the ratchet at strategic scale).
**I/O:** `mass_battle emits scene.battle_concluded` → `consumes` at `peninsular_strain` →
`emits env.peninsular_strain_shock`; a victory yields a *negative* `strain_delta` on **IP** (delay) but rarely
resets it. **Tier:** Active. **Rides:** ② at strategic scale.

**"The General's Duel"** *(scale-transition down; `scale_transitions §3.7 Mass → Personal`).* H: the pre-battle
champion combat (Homeric, medieval trial-by-champion) · L: the single-combat-decides-the-host trope · G: *Total War*
duels / *Mount & Blade*. **Twist:** a mass battle can *resolve down* to a personal_combat scene whose
`scene.combat_resolved` echoes *back up* to the host's morale — a genuine cross-scale hinge the substrate already
supports. **I/O:** `mass_battle → personal_combat (§3.7)` → `scene.combat_resolved → scene.battle_concluded`.
**Tier:** Active event. **Rides:** ④ (the duel is witnessed by two armies — maximal enrollment).

## III.6 Settlements (SE) — culture that drifts as the world worsens

**"Temperament under Strain"** *(Part C's rites fire as α/β-keyed events; the substrate corrupts the culture).*
H: the Chernobyl *samosely* and sacrifice-zone communities · L: the frontier-vigil (the Stillhelm Calamity-vigil,
C.3) · G: *King of Dragon Pass* / *Six Ages* clan-mood events and *Frostpunk* discontent. **Twist:** the
`territory_temperaments §4` drift toward *outcomes-only* under `env.peninsular_strain_shock` is not just a number —
it fires the Part C cultural rites at their outcomes-only register (the vigil becomes grim; the harvest-rite becomes
hoarding). **I/O:** `settlement_layer consumes env.peninsular_strain_shock` → `deterministic_accounting` →
`emits env.population_change + [PROPOSED] scene.settlement_rite`; moves temperament drift, **Order**, **Legitimacy**.
**Tier:** Active event class. **Rides:** ② (strain) + ⑤ (rites carry caste-lived texture).

**"The Enrollment"** *(the Roll of Burghers / granary-count as a settlement action; Griseldis, Mathilde, B.3).*
H: the Venetian *Serrata* / the Roman *annona* grain-audit · L: the census-as-power motif · G: *Pentiment*'s civic
record. **Twist:** ④ — enrollment *constitutes* the right; the un-enrolled Southern Einhir cannot own. **I/O:**
`consumes scene.witness` → `deterministic_accounting` → `emits [PROPOSED] state.witnessed`; moves settlement
**Legitimacy/Popular Support**. **Tier:** Active. **Rides:** ④ + ⑤.

## III.7 Threadwork / World (WR) — the MS engine and the diegetic UI

**"Tending the Wound"** *(the Warden loop that feeds the unowned MS clock; Edeyja/Orm/Torgny, B.4).* H: the reactor
liquidators who maintain what they cannot cure · L: Le Guin's cost-bearing steward · G: *Death Stranding*'s
maintenance-as-play and *Outer Wilds*' attention-driven discovery. **Twist:** deliberate **Regard** (①) of the wound
is what slows MS's −1/year drift; a Warden's death is an MS −2 substrate event (canon, leap-mechanism amendment).
**I/O:** `consumes meta.regarded, meta.thread_woven` → `deterministic_accounting` → `emits [PROPOSED] env.ms_shock`
(the owner-side feed MS currently lacks); moves **MS**, **Coherence**. **Tier:** substrate/Active. **Rides:** ① + ③.

**"The Testament"** *(what persists after a character; companion §3.6).* H: the will/testament and the *ars
moriendi* · L: the memoir-as-accountability instrument · G: *Citizen Sleeper* / roguelike legacy systems. **Twist:**
④ — a Testament rendered and witnessed persists a character's Keys into the world after death (Warden lineages are
*already* mapped onto the MS trajectory). **I/O:** `consumes state.witnessed (at death)` → `state_reader` →
`emits [PROPOSED] meta.testament`; can seed a successor's opening state. **Tier:** Active event. **Rides:** ④ + ①.

## III.8 NPCs — the three-body figures as behavior, not scripting

**"The Observer's Read"** *(Almqvist/Almud as the tertius gaudens made an NPC policy).* H: the intelligence-officer
temperament (Richard Sorge, already Maret Uln's anchor) · L: Smiley's watchfulness · G: *Crusader Kings* AI schemes.
**Twist:** the doctrine guard holds — **no scripting drift**; the "always-wins" is an *emergent* consequence of a
policy that reads the full Key stream and acts last in the Accounting sequence (`E_offscreen`), not a hardcoded
outcome. **I/O:** `npc_behavior consumes * from engine` → `deterministic_accounting` → `emits scene.gossip,
state.opinion_revised`. **Tier:** Active (policy weighting). **Rides:** ② + ①.

---
---

# PART IV — CROSS-SCALE BINDING (why it feels authored, not modular)

The strongest thing the corpus enables is running **one precedent through every scale**, so the game reads as
authored rather than as a bag of minigames. The substrate already carries the hinges: **Domain Echo**
(`scale_transitions §3.4 Scene → Faction`), Thread → Faction/Mass (§3.5/§3.6), Mass → Personal (§3.7), and
Fieldwork ↔ All (§3.9).

**Worked example — the three-body ratchet at four scales (all ② ):**

| Scale | Instance | Rides on |
|---|---|---|
| **Scene (SC)** | A parliamentary contest where Baralta grandstands, Vaynard edits the record, Almqvist subverts both — you extract a local win | `social_contest` → `scene.contest_resolved` |
| **Domain (FA)** | "The Concession" distributes three structural gains and ratchets the floor | `domain_actions` → `da.concession` + `env.peninsular_strain_shock` |
| **Strategic (MB)** | "The Delaying Action" buys IP-clock against Altonia but never resets it | `mass_battle` → `env.peninsular_strain_shock` on **IP** |
| **Settlement (SE)** | Temperament drifts toward outcomes-only as strain climbs; rites sour | `settlement_layer` → temperament drift |

The identical dynamic — *win locally, lose globally, strain climbs monotonically* — rendered at four resolutions.
That echo is exactly what the cross-scale bridge (`parliamentary_bridge` / `scene_dispatch`) exists to carry, and it
is what makes *Disco Elysium* and *Pentiment* feel whole where lesser games feel assembled.

**The coupling that is the whole game:** a mechanic that moves a **political** clock (IP/Turmoil/Mandate/CI) *and*
the **ontological** clock (MS) in one action. "The Examination" (SC) that costs MS on a forced revelation; "Tending
the Wound" (WR) that trades a Warden's life (MS +) against political neglect elsewhere; "The Concession" (FA) whose
strain compounds toward the Second Calamity. **Every such coupling is a place where "who governs" and "whether it
survives" become the same choice** — which is the assessment's thesis, executed.

---
---

# PART V — HOW TO CANONIZE (the honest path)

This brief is a **platform, not a decision**. What each proposal needs to become real:

1. **Declared I/O is proposed, not binding.** Each `[PROPOSED]` Key type (`meta.regarded`, `da.concession`,
   `state.witnessed`, `meta.revelation_rendered`, `state.stance_registered`, `env.ms_shock`, `scene.settlement_rite`,
   `meta.testament`, `state.record_amended`, `state.belief_rendered`) would need a `key_type_registry_v30`
   allocation and a `module_contracts.yaml` edge before it exists. Reused types are already real.
2. **Three dependencies gate the temporal/strategic mechanics** (all already tracked, none invented here):
   - **`engine_clock` is `doc:null`** (ED-1051 open; `propagation_spec_v1` is the candidate home). Anything keyed to
     the Accounting cadence inherits that open item.
   - **`domain_actions` is `doc:null`** and the `da.*` set is an **outcome-tag taxonomy** (ED-FA-0006), not a verb
     module. "The Concession" must be authored as a per-verb tag + crosswalk, consistent with that ruling — and it
     lands naturally on the `domain_actions` home being authored now (**ED-FA-0002**).
   - **MS is an *unowned* clock.** "Tending the Wound" (III.7) proposes the **owner-side feed MS currently lacks** —
     the single highest-leverage substrate opportunity in this brief, because it wires the ontological contest into
     the Key graph for the first time. This is a real design call for Jordan, not a mechanical fill.
3. **Naming + contamination audit.** Any coined proper noun (rites, ledgers, the Testament instrument) is a proposal
   pending `id_reservations.yaml` + the `placeholder_names` audit — the discipline that struck `vaynards_hall`.
4. **Tiering.** Most entries enter as **event classes or resolver modifiers**, not new modules — deliberately, to
   respect the "every rule lives once" invariant and the ~27-module contract surface. Promote to a module only on
   recurrence.

**Recommended first slice.** If one signature substrate is prototyped end-to-end, **② The Ratchet** or **④ The
Ledger-is-real** — both have the most existing corpus to bind to (the FA Parliament prose and the ED-FA-0006 da.*
crosswalk for ②; the Roll of Burghers, the Löwenritter deed-ledger, and `scene.witness`/`settlement Legitimacy` for
④). Either could seed real `ED-FA` / `PP` entries against the `domain_actions` home (ED-FA-0002) without waiting on
`engine_clock`. **The highest-*value* (not lowest-cost) slice is III.7 "Tending the Wound,"** because it is the one
that finally gives the unowned MS clock an owner — but that one is a genuine Jordan design decision, held back here
deliberately, not bundled.

---

*End Precedent → Mechanism Design Brief. SPECULATIVE — proposals and suggestions, ratifying nothing. Declared I/O is
proposed and binds no contract.*
