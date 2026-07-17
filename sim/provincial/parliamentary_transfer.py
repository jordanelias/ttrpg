"""
sim/provincial/parliamentary_transfer.py — Universal CB-required territorial transfer (§§1-4)

Canon source: designs/provincial/parliamentary_transfer_v30.md (CANONICAL, Pass 2h 2026-05-17;
    v12c-balance-validated N=1000). Resolution wraps social_contest_v30 §10 (vote) + §10.1 (stay).
Status: [implemented 2026-05-31 — §1 Pool=Proposer Influence / Ob=Holder Legitimacy + PARL_MAJORITY_OB_BONUS(2),
    §1.2 4-degree outcome, §1.3 protections, §2 four modes, §3 CB sources, §4 vote-wrapped resolution.]

Dependencies:
  - sim/personal/parliamentary_vote   — §10 vote contest (run_parliamentary_vote, Motion, VoteDeclaration)
  - sim/personal/parliamentary_stay   — §10.1 stay hook (available post-roll; caller-invoked per §4 step 7)
  - sim/autoload/dice_engine          — roll_pool + Degree (Continuous Engine, params/core.md)
  - sim/autoload/game_state           — Faction (I/L/Sta/standing/territories), Territory (.accord), ACCORD_MAP, MULTS

Entry point:
  - propose_transfer(initiator, target_territory, mode, world, *, side_a_allies=None,
                     side_b_allies=None, rng=None) -> TransferResult

Mutation: applies effects directly (territory move, L/Sta/Standing deltas, Accord set) AND returns a
TransferResult — matching the sibling faction-action convention (crown_initiative.py adjusts in-place + returns).

[ASSUMPTION: game_state models NO Casus Belli ledger (verified — no casus_belli field). CB is read from an
 OPTIONAL duck-typed world.casus_belli {(proposer,holder): [source,...]} PLUS the one auto-CB the canon makes
 derivable: Crown constitutional restoration when Crown territories < 6 (§3). Without a populated ledger only the
 Crown-restoration path is exercisable; other §3 CB sources require the broader system to populate the ledger.
 Mechanical-tier, Jordan-vetoable.]
[FLAG: §3 "Crown constitutional restoration" CB is not mapped to a mode in §2; mapped here to Adversarial
 (§5: Crown ~60% of attempts, Adversarial ~75% dominant). Confirm.]
[FLAG: vote-bloc -> pool modifier (+1/-1/0) is canon-PROVISIONAL (PARL-VOTE-MODIFIER-001). Bloc defaults to
 proposer(Side A) vs holder(Side B), others abstain; side_a_allies/side_b_allies override. Genre neutral default.]
[FLAG: mode-specific adjustments (Punishment no-L+1/Standing-1; Appeasement +2 Accord; Consensual no holder
 L+1 on Failure) are canon-PROVISIONAL (PARL-MODE-DRIFT-001), implemented as written in §1.2/§2.]
"""
from __future__ import annotations
from dataclasses import dataclass, field

from engine.autoload.dice_engine import roll_pool, Degree
from engine.autoload.game_state import ACCORD_MAP, MULTS
from sim.personal.parliamentary_vote import run_parliamentary_vote, Motion, VoteDeclaration

# ── §1/§3/§5 constants (ledgered) ──
PARL_MAJORITY_OB_BONUS = 2               # [§1.1 Ob = Holder Legitimacy + 2; §5 sensitivity: 2 canonical default]
PARL_TRANSFER_TN = 7                     # [params/core.md §TN Values — standard TN 7 (Continuous Engine)]
PARL_VOTE_POOL_MOD = 1                   # [§4 — majority favoring proposer/holder: Pool +1D / -1D (PROVISIONAL)]
PARL_LAST_TERRITORY_FLOOR = 1            # [§1.3 — cannot strip a faction's last territory]
PARL_TRANSFER_ACCORD = 1                 # [§1.2 — Transferred territory Accord = 1]
PARL_TRANSFER_ACCORD_APPEASEMENT = 2     # [§2 Appeasement — +2 instead of +1 on Success]
PARL_CROWN_RESTORATION_TERRITORY_MAX = 6 # [§3 — Crown constitutional restoration when Crown territories < 6]

MODES = ("adversarial", "consensual", "punishment", "appeasement")

# §2 mode -> qualifying CB sources (§3 source names). crown_constitutional_restoration -> adversarial (FLAG).
_MODE_CB = {
    "adversarial": {"military", "military_conquest", "adjacent_instability",
                    "einhir_revival_partial", "parliamentary_transfer_partial",
                    "crown_constitutional_restoration"},
    "consensual":  {"negotiated_agreement"},
    "punishment":  {"excommunication", "conviction_scar", "treaty_violation"},
    "appeasement": {"crisis_stability", "peninsular_strain_severe",
                    "insurgency_emergence", "war_readiness"},
}


@dataclass
class TransferResult:
    status: str                    # 'transferred' | 'partial' | 'failed' | 'blocked' | 'invalid'
    initiator: str
    target_territory: str
    mode: str
    holder: str | None = None
    degree: object | None = None   # dice_engine.Degree
    vote: object | None = None     # §10 VoteResult
    pool_modifier: int = 0
    pool: int = 0
    ob: int = 0
    cb_used: str | None = None
    effects: list = field(default_factory=list)
    notes: list = field(default_factory=list)


def _holder_of(target_territory, world):
    for name, f in world.factions.items():
        if target_territory in f.territories:
            return name
    return None


def _available_cb(initiator, holder, world):
    """§3 CB sources available to (initiator, holder): auto Crown-restoration + duck-typed ledger."""
    sources = []
    fac = world.factions.get(initiator)
    if (initiator == "Crown" and fac is not None
            and len(fac.territories) < PARL_CROWN_RESTORATION_TERRITORY_MAX):
        sources.append("crown_constitutional_restoration")          # [§3 auto, refreshes per arc]
    ledger = getattr(world, "casus_belli", None)
    if isinstance(ledger, dict):
        sources.extend(ledger.get((initiator, holder), []))
    return sources


def propose_transfer(initiator, target_territory, mode, world, *,
                     side_a_allies=None, side_b_allies=None, rng=None) -> TransferResult:
    """§§1-4: propose a Parliamentary Territory Transfer. CB-gated, vote-wrapped, Influence-vs-Legitimacy roll."""
    res = TransferResult(status="invalid", initiator=initiator, target_territory=target_territory, mode=mode)

    if mode not in MODES:
        res.notes.append(f"invalid mode '{mode}'; expected one of {MODES}")
        return res
    fac = world.factions.get(initiator)
    if fac is None:
        res.notes.append(f"unknown initiator '{initiator}'")
        return res
    # §1.3 / GD-3 — extra-parliamentary cannot initiate.
    if not fac.parliamentary:
        res.status = "blocked"
        res.notes.append(f"GD-3: '{initiator}' extra-parliamentary (parliamentary=False) cannot initiate Parliamentary Transfer.")
        return res

    holder = _holder_of(target_territory, world)
    res.holder = holder
    if holder is None:
        res.notes.append(f"territory '{target_territory}' is unheld; nothing to transfer.")
        return res
    # §1.3 self-transfer block.
    if holder == initiator:
        res.status = "blocked"
        res.notes.append("§1.3 self-transfer block: proposer cannot target their own territory.")
        return res
    # §1.3 last-territory protection (declaration stage; not rolled).
    if len(world.factions[holder].territories) <= PARL_LAST_TERRITORY_FLOOR:
        res.status = "blocked"
        res.notes.append(f"§1.3 last-territory protection: holder '{holder}' has only {len(world.factions[holder].territories)} territory; blocked.")
        return res

    # §1.1/§3 CB prerequisite, mode-filtered (§2).
    available = _available_cb(initiator, holder, world)
    qualifying = [c for c in available if c in _MODE_CB[mode]]
    if not qualifying:
        res.status = "blocked"
        res.notes.append(f"§3 no qualifying CB for mode '{mode}' vs '{holder}' (available: {available or 'none'}).")
        return res
    cb_used = qualifying[0]
    res.cb_used = cb_used

    # §4 step 2-4 — §10 vote contest -> pool modifier. Bloc default proposer(A) vs holder(B) (FLAG: PROVISIONAL).
    motion = Motion(f"parl_transfer_{target_territory}", primary_genre="Memory")
    side_a = [initiator] + list(side_a_allies or [])
    side_b = [holder] + list(side_b_allies or [])
    parties = ([VoteDeclaration(n, "A", motion.primary_genre) for n in side_a]
               + [VoteDeclaration(n, "B", motion.primary_genre) for n in side_b])
    vote = run_parliamentary_vote(motion, parties, world, rng=rng)
    res.vote = vote
    pool_mod = (PARL_VOTE_POOL_MOD if vote.status == "passed"
                else -PARL_VOTE_POOL_MOD if vote.status == "failed" else 0)
    res.pool_modifier = pool_mod

    # §1.1/§4 step 5 — Pool = Proposer Influence + vote mod; Ob = Holder Legitimacy + 2; Continuous Engine.
    pool = max(0, int(fac.I) + pool_mod)
    ob = int(world.factions[holder].L) + PARL_MAJORITY_OB_BONUS
    res.pool, res.ob = pool, ob
    roll = roll_pool(pool_size=pool, tn=PARL_TRANSFER_TN, ob=ob, rng=rng)
    res.degree = roll.degree

    # §3 CB consumption (ledger only; auto Crown-restoration refreshes, not consumed).
    ledger = getattr(world, "casus_belli", None)
    if isinstance(ledger, dict) and cb_used != "crown_constitutional_restoration":
        pair = ledger.get((initiator, holder))
        if pair and cb_used in pair:
            pair.remove(cb_used)

    deg = roll.degree
    holder_fac = world.factions[holder]
    if deg in (Degree.OVERWHELMING, Degree.SUCCESS):
        # §1.2 transfer + Accord set (§2 Appeasement -> 2 instead of 1).
        world.factions[initiator].territories.append(target_territory)
        holder_fac.territories.remove(target_territory)
        terr = world.territories.get(target_territory)
        accord_level = PARL_TRANSFER_ACCORD_APPEASEMENT if mode == "appeasement" else PARL_TRANSFER_ACCORD
        if terr is not None:
            terr.accord = ACCORD_MAP[accord_level]
        res.status = "transferred"
        res.effects.append(f"territory '{target_territory}' transferred {holder}->{initiator}; Accord set {accord_level}.")
        if deg == Degree.OVERWHELMING:
            holder_fac.adjust("L", -1 * MULTS["L"])              # §1.2 Overwhelming — Holder Legitimacy -1
            res.effects.append(f"§1.2 Overwhelming: holder '{holder}' Legitimacy -1.")
    elif deg == Degree.PARTIAL:
        # §1.2 Partial — fail; proposer gains CB vs holder (replaces consumed CB).
        res.status = "partial"
        if isinstance(ledger, dict):
            ledger.setdefault((initiator, holder), []).append("parliamentary_transfer_partial")
        res.effects.append("§1.2 Partial: transfer failed; proposer gains parliamentary_transfer_partial CB for retry next arc.")
    else:  # FAILURE
        res.status = "failed"
        world.factions[initiator].adjust("Sta", -1 * MULTS["Sta"])   # §1.2 Failure — Proposer Stability -1
        res.effects.append(f"§1.2 Failure: proposer '{initiator}' Stability -1.")
        if mode == "punishment":
            holder_fac.standing -= 1                                  # §2 Punishment — Standing -1 (no L+1)
            res.effects.append(f"§2 Punishment: holder '{holder}' Standing -1 (no public-sympathy L+1).")
        elif mode == "consensual":
            res.effects.append("§2 Consensual: holder Legitimacy not damaged/granted on Failure (procedural).")
        else:  # adversarial, appeasement -> default §1.2
            holder_fac.adjust("L", 1 * MULTS["L"])                    # §1.2 Failure — Holder Legitimacy +1
            res.effects.append(f"§1.2 Failure: holder '{holder}' Legitimacy +1 (public sympathy).")
    return res
