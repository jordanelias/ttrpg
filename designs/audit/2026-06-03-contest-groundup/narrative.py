"""
narrative.py — turns a resolved bout into legible, story-shaped output. PURE CONSUMER of the raw beat
log produced by Bout(record=True); it never touches resolution, so it cannot change balance. Depends
only on `contract` (side identity), so it sits at the leaf of the dependency graph.

Products:
  - summarize(log, winner, why)  -> Chronicle   LEGIBILITY: turning point + decisive factor, from data
                                                 the engine already holds but never surfaced.
  - Chronicle.render()           -> str         NARRATIVE CLARITY: a 2-3 sentence story of the bout.
  - classify(...)                -> shape        EMERGENT SCENARIOS: each bout labelled as a recognisable
                                                 arc (ROUT / CLEAR_WIN / NAIL_BITER / REVERSAL / COLLAPSE / DEADLOCK).
  - venue_brief(venue)           -> str         PUBLIC pre-contest cue: what this venue rewards.

All trajectory reasoning is done in EXCHANGE space (end-of-exchange states), so every index the player
sees — turning_point in particular — is a real exchange number, never a beat-list position.

decisive_factor reports what CARRIED the winner's case: the appeal/ground that produced the most of the
winner's *realised* advantage. Realised gain already embeds the judge's reward of that appeal (via
resonance), so it reads as "what worked here", NOT a direct readout of the judge's private leaning — a
signal the player can learn from across bouts, not a guarantee. (See critique 2026-06-04, P1.)
"""
from dataclasses import dataclass, field
from contract import A, B

SHAPES = ("ROUT", "CLEAR_WIN", "NAIL_BITER", "REVERSAL", "COLLAPSE", "DEADLOCK", "SPLIT_DECISION")

# [SEED] Provisional classification thresholds on `margin` (= |advA-advB| / (advA+advB) at close, the
# winner's share of combined advantage). Eyeballed for a plausible scenario spread; NOT anchored to a
# player-perception study or to historical/published-game precedent. Jordan-calibratable. (Critique P2.)
NAIL_MARGIN  = 0.06   # at/below this, razor-thin regardless of lead changes
CLOSE_MARGIN = 0.12   # below this AND with at least one lead change, a nail-biter
ROUT_MARGIN  = 0.30   # above this, with the winner never behind, a rout


def _name(side):
    return "A" if side == A else ("B" if side == B else str(side))


@dataclass
class Chronicle:
    winner: str
    why: str
    shape: str
    margin: float          # |advA-advB| / (advA+advB) at close, in [0,1]; not meaningful for COLLAPSE
    lead_changes: int      # sign changes of (advA-advB) across end-of-exchange states
    turning_point: int     # EXCHANGE index: the comeback crossing (REVERSAL), the clinch (COLLAPSE),
                           #   else the largest end-of-exchange swing
    decisive_appeal: str   # appeal carrying most of the winner's realised advantage; None on a fault win
    decisive_ground: str   # ground most of that advantage accrued on; None on a fault win
    beats: list = field(default_factory=list)
    room_leader: str = None   # side leading on momentum at close; differs from winner only on a SPLIT_DECISION

    def render(self):
        w = _name(self.winner)
        pct = "nothing" if self.margin < 0.005 else f"{self.margin * 100:.0f}%"
        if self.shape == "SPLIT_DECISION":
            room = _name(self.room_leader)
            return (f"[SPLIT DECISION] {room} carried the room by {pct} on momentum, "
                    f"but {w} took the verdict — the vote crossed the room.")
        if self.shape == "DEADLOCK":
            return "[DEADLOCK] Neither side broke ahead; the contest closed level."
        if self.shape == "COLLAPSE":
            reason = self.why.split("clinch:", 1)[1].strip() if "clinch:" in self.why else self.why
            if " - " in reason:
                reason = reason.split(" - ", 1)[1]          # prefer the specific clinch detail over the family
            loser = _name(B if self.winner == A else A)
            return (f"[COLLAPSE] {w} won at exchange {self.turning_point}: {loser} faulted out — {reason}. "
                    f"The merits were never settled.")
        factor = self.decisive_appeal or "accumulated pressure"
        if self.decisive_ground:
            factor += f" on {self.decisive_ground}-ground"
        if self.shape == "REVERSAL":
            return (f"[REVERSAL] {w} came from behind — overtaking at exchange {self.turning_point} "
                    f"after {self.lead_changes} lead-change(s) — and closed {pct} on {factor}.")
        if self.shape == "NAIL_BITER":
            how = f"after {self.lead_changes} lead-change(s)" if self.lead_changes else "decided only at the wire"
            return f"[NAIL-BITER] {pct} separated them at the close, {how}; {w} edged it on {factor}."
        if self.shape == "ROUT":
            return f"[ROUT] {w} led from the opening and never trailed, closing a commanding {pct} on {factor}."
        return f"[CLEAR WIN] {w} took it by {pct}, the case resting on {factor}."


def classify(winner, why, leads, margin, lead_changes, late_crossing):
    """leads: per-EXCHANGE end-state sign of (advA-advB) in {-1,0,1}. A REVERSAL is a genuine late
       comeback — the winner crossed from behind to ahead in the back half — detected from the crossing
       itself, not a single-sample midpoint probe (critique P2). ROUT/NAIL_BITER use the full
       end-of-exchange lead history, not one beat."""
    if winner == "draw" or winner is None:
        return "DEADLOCK"
    if why.startswith("clinch"):
        return "COLLAPSE"                            # ended on a fault, not the merits
    wsign = 1 if winner == A else -1
    if late_crossing:
        return "REVERSAL"
    never_behind = not any(l == -wsign for l in leads)
    if margin < NAIL_MARGIN or (lead_changes >= 1 and margin < CLOSE_MARGIN):
        return "NAIL_BITER"                          # razor-thin, or genuinely swung and stayed close
    if margin > ROUT_MARGIN and never_behind:
        return "ROUT"                                # ahead throughout and pulled clear
    return "CLEAR_WIN"                               # incl. a narrow but controlled, never-trailed win


def _per_exchange(log):
    """Collapse the per-move beat log to end-of-exchange (i, advA, advB) states, in exchange order.
       The last beat written for an exchange index IS that exchange's closing state."""
    end = {}
    for b in log:
        end[b["i"]] = (b["advA"], b["advB"])
    return [(i, end[i][0], end[i][1]) for i in sorted(end)]


def summarize(log, winner, why):
    if not log:
        return Chronicle(winner, why, "DEADLOCK", 0.0, 0, 0, None, None, [], None)
    per = _per_exchange(log)
    diffs = [a - b for (_, a, b) in per]
    leads = [(1 if d > 1e-9 else (-1 if d < -1e-9 else 0)) for d in diffs]
    nz = [x for x in leads if x]
    lead_changes = sum(1 for k in range(1, len(nz)) if nz[k] != nz[k - 1])
    advA, advB = log[-1]["advA"], log[-1]["advB"]
    total = advA + advB
    margin = abs(advA - advB) / total if total else 0.0
    room_leader = A if advA > advB else (B if advB > advA else None)   # who led on momentum at close
    clinch = why.startswith("clinch")
    wside = winner if winner in (A, B) else None
    wsign = 1 if winner == A else (-1 if winner == B else 0)
    # crossings from behind to ahead in the winner's favour, by exchange position
    crossings = [k for k in range(1, len(leads)) if leads[k] == wsign and leads[k - 1] == -wsign]
    late_crossing = (wside is not None and not clinch
                     and any(k >= len(leads) // 2 for k in crossings))
    # turning point — ALWAYS a real exchange index
    if clinch:
        tp = log[-1]["i"]
    elif late_crossing:
        tp = per[crossings[-1]][0]                       # the decisive comeback exchange
    else:
        sw = [(abs(diffs[k] - (diffs[k - 1] if k else 0.0)), per[k][0]) for k in range(len(diffs))]
        tp = max(sw)[1] if sw else (per[0][0] if per else 0)
    # decisive factor — most of the winner's REALISED advantage, by appeal/ground. None on a fault win
    # (there the win is the opponent's fault, so the winner's own gains carry no story — critique P1).
    dec_a = dec_g = None
    if wside is not None and not clinch:
        appeal_c, ground_c = {}, {}
        for b in log:
            if b["side"] == wside and b["gain"] > 0:
                appeal_c[b["appeal"] or "logos"] = appeal_c.get(b["appeal"] or "logos", 0.0) + b["gain"]
                if b["ground"]:
                    ground_c[b["ground"]] = ground_c.get(b["ground"], 0.0) + b["gain"]
        dec_a = max(appeal_c, key=appeal_c.get) if appeal_c else None
        dec_g = max(ground_c, key=ground_c.get) if ground_c else None
    shape = classify(winner, why, leads, margin, lead_changes, late_crossing)
    if not clinch and winner in (A, B) and room_leader in (A, B) and winner != room_leader:
        shape = "SPLIT_DECISION"        # the verdict crossed the room (only reachable under VoteAtClose)
    return Chronicle(winner, why, shape, margin, lead_changes, tp, dec_a, dec_g, list(log), room_leader)


def venue_brief(venue):
    """PUBLIC pre-contest cue — what everyone knows about this venue (its declared norms), NOT the
       judge's private character. [SEED] design assumption: venue weights are player-visible while the
       individual adjudicator's leaning is hidden and learned through play. Jordan to confirm the split."""
    role, tw = venue.role(), venue.tense_weight()
    la, lt = max(role, key=role.get), max(tw, key=tw.get)
    f = venue.faults
    fatal = []
    if f.barred:          fatal.append("overreach")
    if f.contradiction:   fatal.append("self-contradiction")
    if f.evasion_strikes: fatal.append(f"evasion(x{f.evasion_strikes})")
    if f.yield_strikes:   fatal.append(f"silence(x{f.yield_strikes})")
    return (f"rewards {la}; favours {lt}-ground argument; opens on {venue.start_ground}; "
            f"fatal: {', '.join(fatal) or 'none'}")
