"""
Valoria Campaign Simulation — Game State (Phase 4.1)
All values initialized from canonical design docs.
"""
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import math, random

@dataclass
class Settlement:
    name: str
    territory: str
    type: str  # Seat, City, Town, Fortress, Cathedral, Port, Mine, Outpost
    prosperity: int = 2
    defense: int = 2
    order: int = 3
    controller: str = ''
    governor: str = ''
    church_building: bool = False
    church_templar: bool = False
    church_inquisitor: bool = False
    church_governor: bool = False

    @property
    def local_economy(self): return self.prosperity * 50
    @property
    def garrison_strength(self): return self.defense * 20
    @property
    def public_order(self): return self.order * 20

@dataclass
class Faction:
    name: str
    mandate: int = 4
    wealth: int = 4
    military: int = 4
    influence: int = 4
    stability: int = 4
    territories: List[str] = field(default_factory=list)
    active: bool = True
    # Derived values
    treasury: float = 0
    legitimacy: float = 0
    reputation: float = 0
    cohesion: float = 0

    def init_derived(self):
        self.treasury = self.wealth * 100
        self.legitimacy = self.mandate * 20
        self.reputation = self.influence * 15
        self.cohesion = self.stability * 10

    @property
    def levies_available(self): return self.military * 2

@dataclass
class NPC:
    name: str
    faction: str
    primary_conviction: str = ''
    secondary_conviction: str = ''
    primary_rs: str = ''  # Resonant Style
    secondary_rs: str = ''
    ts: int = 0  # Thread Sensitivity
    certainty: int = 3
    disposition: int = 0  # toward PC
    scars: int = 0
    arc_position: str = 'A'
    alive: bool = True
    coherence: int = 10
    beliefs: List[str] = field(default_factory=list)

@dataclass
class PC:
    faction: str = 'Crown'
    # Attributes (1-7)
    spirit: int = 4
    focus: int = 4
    attunement: int = 4
    cognition: int = 4
    charisma: int = 4
    bonds: int = 3
    recall: int = 3
    # State
    ts: int = 0
    certainty: int = 3
    coherence: int = 10
    standing: int = 0
    renown: int = 0
    momentum: int = 0
    resources: int = 2
    wounds: int = 0
    stamina: int = 0
    exposure: Dict[str, int] = field(default_factory=dict)
    convictions: List[str] = field(default_factory=list)
    knots: List[str] = field(default_factory=list)
    companions: List[str] = field(default_factory=list)

@dataclass
class GameState:
    season: int = 0
    # Global clocks
    rs: int = 72    # Rendering Stability
    tc: int = 28    # Church Influence
    ip: int = 5     # Institutional Pressure
    pi: int = 7     # Peninsular Integration
    strain: int = 0
    # Collections
    factions: Dict[str, Faction] = field(default_factory=dict)
    settlements: List[Settlement] = field(default_factory=list)
    npcs: Dict[str, NPC] = field(default_factory=dict)
    pc: PC = field(default_factory=PC)
    # Per-territory
    pt: Dict[str, int] = field(default_factory=dict)  # Piety Track
    # Co-Movement deck
    cm_deck: List[int] = field(default_factory=list)
    cm_drawn: int = 0
    # Domain Echo queue
    echo_queue: List[dict] = field(default_factory=list)
    # Event log
    log: List[str] = field(default_factory=list)
    # Feature coverage bitmap
    features_fired: set = field(default_factory=set)

    def get_province_accord(self, territory: str) -> int:
        """Province Accord = floor(mean settlement Order) per settlement_layer §1.3"""
        t_settlements = [s for s in self.settlements if s.territory == territory]
        if not t_settlements:
            return 0
        return math.floor(sum(s.order for s in t_settlements) / len(t_settlements))


def init_game_state(pc_faction='Crown', seed=42) -> GameState:
    """Initialize game state from canonical values (workplan §4.1)."""
    random.seed(seed)
    gs = GameState()

    # Factions (workplan §4.1 table)
    gs.factions = {
        'Crown':    Faction('Crown',    mandate=5, wealth=4, military=4, influence=5, stability=4,
                           territories=['T1','T2','T3','T5','T6','T14']),
        'Church':   Faction('Church',   mandate=4, wealth=3, military=4, influence=6, stability=5,
                           territories=['T9']),
        'Hafenmark':Faction('Hafenmark',mandate=4, wealth=5, military=3, influence=4, stability=4,
                           territories=['T7','T8','T10','T17']),
        'Varfell':  Faction('Varfell',  mandate=3, wealth=3, military=4, influence=3, stability=3,
                           territories=['T4','T11','T12','T13']),
        # Dormant factions
        'Lowenritter': Faction('Lowenritter', active=False),
        'RM':          Faction('RM', active=False),
        'Altonian':    Faction('Altonian', active=False),
        'Wardens':     Faction('Wardens', active=False),
    }
    for f in gs.factions.values():
        if f.active:
            f.init_derived()

    # Settlements (simplified — representative sample per territory)
    settlement_data = [
        # Crown
        ('Valorsplatz', 'T1', 'Seat', 3, 3, 4, 'Crown'),
        ('Kronburg', 'T1', 'City', 2, 2, 3, 'Crown'),
        ('Nordheim', 'T2', 'Town', 2, 1, 3, 'Crown'),
        ('Altfeld', 'T2', 'Fortress', 1, 4, 3, 'Crown'),
        ('Westmark', 'T3', 'City', 3, 2, 3, 'Crown'),
        ('Grenzburg', 'T3', 'Town', 2, 1, 3, 'Crown'),
        ('Steinfeld', 'T3', 'Outpost', 1, 3, 2, 'Crown'),
        ('Hohenpass', 'T5', 'Town', 2, 2, 3, 'Crown'),
        ('Grautal', 'T5', 'Mine', 1, 1, 2, 'Crown'),
        ('Ehrenfeld', 'T6', 'Fortress', 1, 4, 2, 'Crown'),
        ('Dunkelwald', 'T6', 'Outpost', 0, 2, 1, 'Crown'),
        ('Sudmark', 'T14', 'Town', 2, 1, 3, 'Crown'),
        ('Grenzwacht', 'T14', 'Outpost', 1, 3, 2, 'Crown'),
        # Church
        ('Himmelenger', 'T9', 'Cathedral', 3, 2, 4, 'Church'),
        ('Pilgerstadt', 'T9', 'City', 2, 1, 3, 'Church'),
        ('Klosterdorf', 'T9', 'Town', 2, 1, 3, 'Church'),
        # Hafenmark
        ('Hafenstadt', 'T7', 'Port', 5, 2, 4, 'Hafenmark'),
        ('Handelsplatz', 'T7', 'City', 3, 1, 3, 'Hafenmark'),
        ('Baralta', 'T8', 'Seat', 4, 3, 4, 'Hafenmark'),
        ('Markthof', 'T8', 'Town', 2, 1, 3, 'Hafenmark'),
        ('Seeheim', 'T10', 'Port', 3, 2, 3, 'Hafenmark'),
        ('Feldkirch', 'T10', 'Town', 2, 1, 3, 'Hafenmark'),
        ('Osthafen', 'T10', 'Outpost', 1, 2, 2, 'Hafenmark'),
        ('Schoenland', 'T17', 'City', 3, 2, 3, 'Hafenmark'),
        ('Grenzhafen', 'T17', 'Town', 2, 1, 3, 'Hafenmark'),
        # Varfell
        ('Jarlshall', 'T4', 'Seat', 2, 3, 3, 'Varfell'),
        ('Fjordheim', 'T4', 'Town', 1, 1, 2, 'Varfell'),
        ('Hochheim', 'T11', 'City', 3, 2, 3, 'Varfell'),
        ('Bergdorf', 'T11', 'Mine', 1, 1, 2, 'Varfell'),
        ('Eismark', 'T12', 'Fortress', 1, 4, 2, 'Varfell'),
        ('Frostheim', 'T12', 'Outpost', 0, 2, 1, 'Varfell'),
        ('Waldheim', 'T13', 'Town', 2, 1, 2, 'Varfell'),
        ('Grenzdorf', 'T13', 'Outpost', 1, 2, 2, 'Varfell'),
        ('Nebeltal', 'T13', 'Mine', 0, 1, 1, 'Varfell'),
    ]
    for name, terr, stype, p, d, o, ctrl in settlement_data:
        gs.settlements.append(Settlement(name, terr, stype, p, d, o, ctrl))

    # PT per territory
    gs.pt = {f'T{i}': 3 for i in range(1, 18)}
    gs.pt['T9'] = 5   # Cathedral
    gs.pt['T6'] = 1   # Low piety frontier
    gs.pt['T13'] = 1  # Varfell
    gs.pt['T4'] = 2
    gs.pt['T11'] = 2
    gs.pt['T12'] = 2
    gs.pt['T15'] = 0  # Askeheim hard-fixed

    # NPCs (14 named, from npc_behavior §2)
    npc_data = [
        ('Almud', 'Crown', 'Order', 'Reason', 'Authority', 'Evidence', 0, 3),
        ('Ehrenwall', 'Crown', 'Order', 'Autonomy', 'Authority', 'Consequence', 0, 4),
        ('Torben', 'Crown', 'Faith', 'Order', 'Authority', 'Solidarity', 0, 4),
        ('Vossen', 'RM', 'Justice', 'Autonomy', 'Solidarity', 'Evidence', 40, 2),
        ('Hann', 'RM', 'Justice', 'Faith', 'Evidence', 'Solidarity', 15, 2),
        ('Baralta', 'Hafenmark', 'Order', 'Justice', 'Authority', 'Evidence', 0, 3),
        ('Heljason', 'Hafenmark', 'Justice', 'Autonomy', 'Evidence', 'Consequence', 0, 3),
        ('Vaynard', 'Varfell', 'Reason', 'Autonomy', 'Evidence', 'Consequence', 50, 1),
        ('Maret Uln', 'Varfell', 'Justice', 'Reason', 'Solidarity', 'Evidence', 35, 2),
        ('Confessor', 'Church', 'Faith', 'Order', 'Authority', 'Authority', 0, 5),
        ('Jarnstal', 'Church', 'Faith', 'Order', 'Authority', 'Consequence', 0, 5),
        ('Olafsson', 'Church', 'Faith', 'Justice', 'Authority', 'Evidence', 0, 5),
        ('Tormann', 'Church', 'Faith', 'Order', 'Authority', 'Consequence', 0, 4),
        ('Klapp', 'Church', 'Reason', 'Faith', 'Evidence', 'Authority', 10, 3),
    ]
    for name, fac, pc, sc, prs, srs, ts, cert in npc_data:
        gs.npcs[name] = NPC(name, fac, pc, sc, prs, srs, ts, cert)

    # PC
    gs.pc = PC(faction=pc_faction)

    # Co-Movement deck (18 cards, shuffled)
    gs.cm_deck = list(range(1, 19))
    random.shuffle(gs.cm_deck)

    return gs
