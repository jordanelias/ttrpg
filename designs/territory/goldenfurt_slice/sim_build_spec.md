# Goldenfurt Governance — Sim Build Spec

**Goal:** make the governance loop (`governance_play_redesign_v1.md`) and the Goldenfurt slice run in code. This **closes audit gap G1** (no settlement registry; `sim/territory/settlement.py` is a 1:1 territory→settlement stub) — which is the prerequisite for everything else here.
**Style:** matches the existing `sim/territory/` modules (dataclasses, module-level fallback store that migrates to `World`, `[canonical: §X]` annotations).

---

## 1. Settlement registry (closes G1)

New module `sim/territory/registry.py`. `Settlement` carries every field the deck predicates and NPC dossiers reference.

```python
@dataclass
class LedgerTag:
    kind: str          # "Precedent" | "Grudge" | "Debt" | "Reputation" | "Leverage"
    key: str           # e.g. "only-sons-exempt", "Hedda", "konrad-corrupt"
    value: float = 1.0
    created_season: int = 0
    ttl: int | None = None   # None = durable (survives succession)

@dataclass
class Settlement:
    sid: str                       # "S-006"
    name: str                      # "Goldenfurt"
    stype: str                     # §1.2 type — "Town"
    province_id: str               # "Kronmark" / "T2"
    owner_faction: str             # Provincial Authority = "Crown"
    governor_id: str | None        # NPC/PC id currently governing
    # §1.3 stats (0-5)
    prosperity: int = 3
    defense: int = 1
    order: int = 2
    fort_level: int = 0
    garrison: bool = False
    # §1.8 per-settlement political acceptance (0-7)
    legitimacy: int = 3            # L
    popular_support: int = 3       # PS
    # §1.4 / governance economy
    facility_tier: int = 1         # 0-3 → AP = 2 + facility_tier
    suspicion: int = 0             # Provincial-Authority distrust (Directive defiance)
    pressure: float = 4.0          # Π, 0-10
    # [verify fix sim-F1/F2/F3/F5/F7/F9] fields the deck/dossiers trigger on
    active_directive: str | None = None   # current-season Directive type; deck reads `directive == ...`
    religious_building: str = "Chapel"    # None|Chapel|Church|Cathedral — the Geneva arc (G204→G603 mutates)
    church_attention: int = 0      # rises on RM-shelter / Wessel denunciation / G605 rite; drives the Suppress Directive
    governor_emergence: int = 0    # player faction-emergence Stage 2→3 progress (G303/G601/G606 increment)
    treasury_source: str = "owner_faction"   # settlement spend draws from world.factions[owner].treasury
    open_needs: list = field(default_factory=list)   # [(card_id, pressure_if_ignored)] drawn-but-unserved; Π reads the remainder
    # presences + relational
    subnational: dict[str, int] = field(default_factory=dict)   # {"Guild":1,"Church":1,"RM":1(covert),"Niflhel":1(covert)}
    npc_ids: list[str] = field(default_factory=list)            # ["NPC-G01",...]
    ledger: list[LedgerTag] = field(default_factory=list)
    deck_state: dict = field(default_factory=dict)              # cooldowns, fired-once, queued-forced-cards

    @property
    def ap(self) -> int:
        return 2 + self.facility_tier + (1 if self.stype in ("Seat", "Cathedral") else 0)

    def has_tag(self, kind: str, key: str | None = None) -> bool: ...
    def tags(self, kind: str) -> list[LedgerTag]: ...
    def add_tag(self, tag: LedgerTag) -> None: ...   # dedupes by (kind,key)
```

**World integration.** Add `World.settlements: dict[str, Settlement]`. Seed via `populate_settlements(world, registry_path)` reading `settlement_layer §2.1` (or the machine mirror `npc_roster.yaml` + a `settlements.yaml`). **Backward-compat for `settlement.py`:** `compute_settlement_state(sid, world)` returns from `world.settlements[sid]` when present, else falls back to today's territory derivation — so nothing that currently calls the stub breaks. Province aggregation (`aggregate_to_province`, §1.3 floor-avg) now iterates the *real* member settlements instead of the synthetic single one — this is what the floor-average was always meant to do.

---

## 2. Ledger (durable settlement memory)

Ledger tags live on `Settlement.ledger`, **not on the governor**, so they survive succession (the next governor inherits the town's memory — the player→world persistence guarantee). Helpers above. `Reputation:*` is single-valued (latest wins); `Precedent`/`Grudge`/`Debt`/`Leverage` accumulate. TTL lets transient tags expire in the Accounting sweep.

---

## 3. Governance verbs + AP economy

New module `sim/territory/governance.py`. Each verb is a pure function `(settlement, world, *opts) -> GovResult` returning stat deltas, ledger writes, Π delta, and NPC-disposition deltas — applied atomically, AP-gated.

```python
@dataclass
class GovResult:
    ok: bool; ap_spent: int
    stat_deltas: dict; ledger_writes: list[LedgerTag]
    pressure_delta: float; disposition_deltas: dict; narrative: str

def develop(s, world, *, funding: str) -> GovResult:   # funding in {"treasury","guild","corvee"}
    # guild -> subnational["Guild"] += 1 + Precedent:"guild-charter-pressure"; corvee -> order -= 1 ...
```

Signatures for all eight: `develop, fortify, keep_order(method), hold_court(dispute, ruling), sponsor(target), treat(faction), levy(kind), investigate(target)`. The AP budget (`s.ap`) is checked by a `GovernanceTurn` controller that accepts a list of `(verb, opts)` and rejects over-budget plans. **Every verb writes at least one world-delta** (stat / ledger / disposition) — the churn invariant, asserted in tests.

---

## 4. Directive generator (the dual-authority engine)

New module `sim/factions/directives.py`.

```python
@dataclass
class Directive:
    dtype: str   # "Extract"|"Tax"|"Suppress"|"Install"|"Host"|"Cede"
    target_sid: str; terms: dict; issued_season: int

def issue_directive(s, world) -> Directive:
    pa = world.factions[s.owner_faction]
    # read the PA priority tree (npc_behavior §8.2): at_war -> Extract; low_treasury -> Tax;
    # RM_present & high church_attention -> Suppress; ...
    # [verify fix CG-3] fallback -> a low-stakes Directive (Census/Host/Tax-light) — NEVER "none":
    # the mandatory world->player stroke must never be skipped.

def resolve_directive(s, world, response: str) -> GovResult:
    # response in {"comply","bargain","defy"}; comply -> +Standing, strain; defy -> suspicion+1,
    # PS+, advances Konrad(G06).progress; bargain -> social_contest(§7) to soften.
```

The Directive is the mandatory world→player move each season; the response feeds `suspicion`, L/PS, and the Konrad ambition tick.

---

## 5. Event-deck engine

New package `sim/territory/events/`:

- **`deck.py`** — `EventCard` (loaded from `*.deck.yaml`), `CardStore`, and `draw(s, world, rng)`:
  1. `n = 1 + floor(s.pressure / 3)` (clamped ≥1, the anti-stall floor).
  2. candidate = cards whose `triggers` all pass the predicate evaluator, minus cooldown/excluded/queued-forced.
  3. weight each = `base + pressure_scaling(family, s.pressure) + tag_modifiers`. Low Π biases `Opportunity`/`Ambition`; high Π biases `Crisis`.
  4. always prepend any **forced** cards (queued Ambition fires from §6, mandatory Directive friction).
- **`predicates.py`** — `evaluate(expr: str, ctx) -> bool` over a safe context (`Order`, `Prosperity`, `Π`, `directive`, `tag(...)`, `npc(id).disp`, `npc(id).progress`). A small expression grammar (comparisons + `AND`/`OR`/`has_tag`), no `eval`.
- **`pressure.py`** — the homeostat:

```
Π_next = clamp(
    Π
    + Σ_unserved_needs          # each Need not addressed this season: +pressure_if_ignored
    + Σ_active_grudges          # +0.5 per Grudge tag
    + Σ_ambitions_in_motion     # +0.5 per NPC with progress > 0 and not firing
    + external_shock            # province war / calamity bleed
    - Σ_player_releases         # the pressure_delta of every response taken
    + restore_toward(3)         # [verify fix CG-1] BIDIRECTIONAL: +1 toward 3 when Π<3, -1 when Π>3
, 0, 10)
# restore_toward(3) := sign(3 - Π) * min(1, abs(3 - Π))  — anti-runaway above the band, ANTI-STALL below it.
# (The earlier `- decay_toward(3)` was mis-signed: it only pulled DOWN, pinning a quiet town toward Π=0.)
# ANTI-STALL also: draw is floored at 1 and low-Π draws are biased to Opportunity/Ambition,
# so a "solved" town keeps moving (the world offers instead of threatening).
```

---

## 6. NPC ambition tick (the world's initiative)

NPCs carry runtime ambition state (`progress`, `firing`). Add an Accounting step (`sim/peninsular/accounting.py`, the 13-step cascade):

```python
def tick_ambitions(world):                      # [canonical: governance_play_redesign §3.2]
    for s in world.settlements.values():
        for nid in s.npc_ids:
            npc = world.npcs[nid]
            if npc.ambition and not npc.ambition.firing:
                npc.ambition.progress += advance_amount(npc, s, world)   # per the dossier predicate
                if npc.ambition.progress >= npc.ambition.timeline:
                    npc.ambition.firing = True
                    s.deck_state.setdefault("forced", []).append(npc.ambition.fires_card)  # G60x next draw
```

This is what makes ignoring the ambitious Magistrate produce a Magistrate who, four seasons later, has the votes (`G601`) — the world moving on its own clock.

---

## 7. Build sequence (dependency-ordered)

| Step | Deliverable | Depends on |
|------|-------------|-----------|
| **S0** | `registry.py` `Settlement` + `World.settlements` + `populate_settlements`; `settlement.py` reads registry (closes G1) | — |
| **S1** | `LedgerTag` + helpers + Accounting TTL sweep | S0 |
| **S2** | `governance.py` 8 verbs + AP controller | S0, S1 |
| **S3** | `directives.py` generator + comply/bargain/defy + suspicion | S0, S2 |
| **S4** | `events/` deck engine: loader, predicates, `pressure.py` homeostat, `draw` | S1 |
| **S5** | `tick_ambitions` in Accounting; NPC ambition runtime state | S0, S4 |
| **S6** | Wire into the season loop; ship the Goldenfurt content pack (`goldenfurt.deck.yaml`, `goldenfurt_npcs.yaml`) | S2–S5 |

## 8. File changes

- **new:** `sim/territory/registry.py`, `sim/territory/ledger.py`, `sim/territory/governance.py`, `sim/territory/events/__init__.py`, `sim/territory/events/deck.py`, `sim/territory/events/predicates.py`, `sim/territory/events/pressure.py`, `sim/factions/directives.py`
- **modify:** `sim/autoload/game_state.py` (`World.settlements`, `World.npcs` ambition runtime), `sim/territory/settlement.py` (registry-backed path + real multi-settlement `aggregate_to_province`), `sim/peninsular/accounting.py` (TTL sweep + `tick_ambitions`)
- **content:** `designs/territory/goldenfurt_slice/content/goldenfurt.deck.yaml`, `goldenfurt_npcs.yaml`, `settlements_seed.yaml`
- **index:** update `canon/mechanics_index.yaml` — add `settlement_registry`, `governance_verbs`, `event_deck`, `directive_generator`, `npc_ambition` entries (and fix the audit D4 `not_implemented`/`Population`/`Forts` staleness while touching it).

## 9. Test plan

- **S0:** `compute_settlement_state("S-006", world)` reads the registry; `aggregate_to_province("Kronmark")` averages 3 real settlements, not 1.
- **S1:** a `Precedent` tag written under governor A is still present after `succeed_governor(A→B)`.
- **S2:** `develop(funding="guild")` raises `subnational["Guild"]` and writes `Precedent:guild-charter-pressure`; AP controller rejects a 4-AP plan at 3 AP.
- **S3:** `resolve_directive(defy)` raises `suspicion` and advances `NPC-G06.progress`.
- **S4:** at Π=1 the draw returns 1 card biased Opportunity/Ambition (anti-stall); at Π=9 it returns 4 biased Crisis; a card on cooldown never draws; Π decays toward 3.
- **S5:** ignoring `NPC-G01` four seasons fires `EVT-G601` into the forced queue.
- **Integration (the acceptance test):** replay the two-season churn trace in `event_deck.md` and assert the resulting world-state (suspicion +1, Hedda.Disp +2, `Precedent:only-sons-exempt`, then `G303`+`G502` drawn in S2, `Leverage:konrad-corrupt` obtainable).

## 10. Open risks

- **Predicate language scope creep** — keep `predicates.py` a tiny grammar; do not let cards smuggle arbitrary logic. If a card needs real logic, it's a coded handler, not a predicate string.
- **Content volume** — a "robust" deck is ~60–100 base cards + type modifiers; Goldenfurt's 28 is one settlement-type's worth. Budget authoring time per settlement type.
- **AI Directive quality** — the whole dual-authority tension is only as good as the PA priority tree's Directive choices; this is the same lesson the genre comparison flagged (governance needs scheming AI). Prioritize S3 quality.
- **Π tuning** — the homeostat band (baseline 3, decay 1) is a guess; needs a sim sweep against "is the town ever boring / ever an unsurvivable spiral?"
- **Balance scalars still TBD upstream** — `political_value` (§2.4) and fracturing triggers (§2.3) remain unspecified in canon; this slice runs without them but the strategic layer above it doesn't fully close until they land.
