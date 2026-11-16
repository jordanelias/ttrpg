"""The data, transcribed from the spec. Each block cites its table. Values here are the TABLE cells; which column
(control / shipped) a run uses is `dials.py`'s choice. The module (`proceeding.py`) reads none of this: the host
(`host.py`) hands it in, as RD A.3 says ("the module holds no roster").
"""
from __future__ import annotations

# RD B.2 a content-class table (RD:527-533) / PLAN B24p.01 item 1 (part22_b24p.md:89): w_reason control 1.0, shipped:
CONTENT_CLASSES_SHIPPED = {"evidentiary": 0.8, "logical": 0.7, "procedural": 0.6, "appeal": 0.4, "emotional": 0.2}
CONTENT_CLASSES_CONTROL = {k: 1.0 for k in CONTENT_CLASSES_SHIPPED}

# PLAN B24p.01 item 1 `grounds` (ordered) with RD B.3's derivation table (RD:643-648)
GROUNDS = (
    {"id": "evidence",    "read": ("attribute", "reason"),     "trait": "moved_by_evidence",    "content": "evidentiary"},
    {"id": "consequence", "read": ("pursuit", "strongest"),    "trait": "moved_by_consequence", "content": "logical"},
    {"id": "authority",   "read": ("conviction", "strongest"), "trait": "moved_by_authority",   "content": "appeal"},
    {"id": "solidarity",  "read": ("attribute", "attunement"), "trait": "moved_by_solidarity",  "content": "emotional"},
)
GROUND_IDS = tuple(g["id"] for g in GROUNDS)

# RD C.4 table (part2:122-129) + PLAN B24p.01's extra cells (fit, holds, effect, ploy, difficulty, content)
PROCEEDING_MOVES = (
    {"id": "argue",   "draw": True,  "capability": "argue",     "resisted_by": "will",       "ground": True,
     "fit": True,  "holds": False, "effect": "track",  "ploy": False, "difficulty": 0.0},
    {"id": "press",   "draw": True,  "capability": "argue",     "resisted_by": "will",       "ground": True,
     "fit": False, "holds": False, "effect": "strike", "ploy": False, "difficulty": 0.0},
    {"id": "divert",  "draw": True,  "capability": "argue",     "resisted_by": "will",       "ground": False,
     "fit": False, "holds": False, "effect": "pull",   "ploy": True,  "difficulty": 0.0, "content": "procedural"},
    {"id": "deceive", "draw": True,  "capability": "deception", "resisted_by": "attunement", "ground": True,
     "fit": True,  "holds": True,  "effect": "track",  "ploy": True,  "difficulty": 0.0},
    {"id": "concede", "draw": False, "capability": None,        "resisted_by": None,         "ground": False,
     "fit": False, "holds": False, "effect": "yield",  "ploy": False, "difficulty": 0.0},
    {"id": "rest",    "draw": False, "capability": None,        "resisted_by": None,         "ground": False,
     "fit": False, "holds": False, "effect": "none",   "ploy": False, "difficulty": 0.0},
)
MOVES_BY_ID = {m["id"]: m for m in PROCEEDING_MOVES}

# RD A.5 / PLAN B24p.01: proceeding_ends (closed)
PROCEEDING_ENDS = ("budget", "rested", "yielded", "broken", "struck", "adjourned")

# PLAN B24p.01: authorities + by_faction [ASSUMPTION; Jordan to correct]
AUTHORITIES = ("parties", "polity", "church", "guild", "none")
AUTHORITY_BY_FACTION = {"Crown": "polity", "Parliament": "polity", "duchy": "polity", "Church": "church",
                        "Guild": "guild"}           # "any other -> polity"

# RD C.4 rites (part2:141-146)
RITES = {
    "contest":    {"for": ("argue", "press", "divert", "concede", "rest"),
                   "against": ("argue", "press", "divert", "concede", "rest"), "bench": (), "faults": ()},
    "address":    {"for": ("argue", "rest"), "against": (), "bench": (), "faults": ()},
    "questioned": {"for": ("argue", "press", "rest"), "against": ("argue", "concede", "rest"), "bench": (),
                   "faults": ()},
    "plain":      {"for": ("argue",), "against": (), "bench": (), "faults": ()},
}

# RD C.5 audience_kinds (part2:172-177); control: attention 0, distraction 0, proof_weight 0.5 on every kind
AUDIENCE_KINDS_SHIPPED = {
    "none":    {"attention": 0.0, "distraction": 0.5,  "proof_weight": 0.5},
    "bench":   {"attention": 2.0, "distraction": 0.25, "proof_weight": 0.75},
    "gallery": {"attention": 4.0, "distraction": 0.5,  "proof_weight": 0.5},
    "crowd":   {"attention": 5.0, "distraction": 1.0,  "proof_weight": 0.25},
}
AUDIENCE_KINDS_CONTROL = {k: {"attention": 0.0, "distraction": 0.0, "proof_weight": 0.5} for k in AUDIENCE_KINDS_SHIPPED}

# RD B.2 a venue table (RD:535-541): reason_bias, shipped (control 0 on every row)
REASON_BIAS_SHIPPED = {
    "legal_trial": 0.2, "tribunal": 0.2, "inquisition_hearing": 0.2,
    "arbitration": 0.1, "interrogation": 0.1, "excommunication_deliberation": 0.1, "council_of_state": 0.1,
    "conversation": 0.0, "questioning": 0.0, "negotiation": 0.0, "audience": 0.0,
    "parliamentary_debate": -0.1,
    "rally": -0.3,
}

# RD C.3 (part2:70-84): the thirteen rows. `standard` = the column B24p.23 sets (control: B05.21 ships every row
# `plain`; B24p.03 writes `plain` on the four new rows). `proofs`/`quorum`/`bench_basis` from arrangements.yaml (tree)
# for the nine; the four new rows per B24p.03 item 3. parliamentary_debate: "bench, to be `declared`" -> bench (C.3 note).
ROWS = {
    "conversation": dict(authority="parties", venue_min_rank="hearth", standard="plain", floor="closed",
                         order="alternating", exchanges=(1, 3), rite="contest", disposal="hearers", presumes="none",
                         strikes=0, disposes="none", quorum=None, proofs=(), bench_basis="none"),
    "questioning": dict(authority="parties", venue_min_rank="hearth", standard="plain", floor="closed",
                        order="scripted", exchanges=(1, 4), rite="questioned", disposal="hearers", presumes="none",
                        strikes=0, disposes="none", quorum=None, proofs=(), bench_basis="none"),
    "rally": dict(authority="none", venue_min_rank="hearth", standard="plain", floor="open", order="free",
                  exchanges=(1, 3), rite="address", disposal="hearers", presumes="none", strikes=0, disposes="none",
                  quorum=None, proofs=(), bench_basis="none"),
    "audience": dict(authority="polity", venue_min_rank="settlement", standard="demanding", floor="admitted",
                     order="free", exchanges=(1, 2), rite="address", disposal="bench", presumes="against", strikes=0,
                     disposes="oblige", quorum=None, proofs=(), bench_basis="determine"),
    "negotiation": dict(authority="parties", venue_min_rank="hearth", standard="plain", floor="closed",
                        order="alternating", exchanges=(1, 3), rite="contest", disposal="mutual", presumes="none",
                        strikes=0, disposes="oblige", quorum=None, proofs=("record", "testimony"), bench_basis="none"),
    "arbitration": dict(authority="parties", venue_min_rank="hearth", standard="routine", floor="closed",
                        order="alternating", exchanges=(2, 3), rite="contest", disposal="bench", presumes="none",
                        strikes=2, disposes="oblige", quorum=None, proofs=("record", "testimony", "oath"),
                        bench_basis="determine"),
    "legal_trial": dict(authority="polity", venue_min_rank="settlement", standard="demanding", floor="open",
                        order="rank", exchanges=(2, 5), rite="contest", disposal="bench", presumes="none", strikes=2,
                        disposes="detain", quorum=None, proofs=("record", "testimony", "oath"), bench_basis="determine"),
    "tribunal": dict(authority="polity", venue_min_rank="settlement", standard="demanding", floor="admitted",
                     order="rank", exchanges=(2, 4), rite="contest", disposal="bench", presumes="none", strikes=2,
                     disposes="ban", quorum=None, proofs=("record", "testimony", "oath"), bench_basis="determine"),
    "interrogation": dict(authority="polity", venue_min_rank="hearth", standard="plain", floor="closed",
                          order="scripted", exchanges=(1, 4), rite="questioned", disposal="bench", presumes="for",
                          strikes=1, disposes="detain", quorum=None, proofs=("testimony", "confession"),
                          bench_basis="determine"),
    "inquisition_hearing": dict(authority="church", venue_min_rank="settlement", standard="hard", floor="closed",
                                order="scripted", exchanges=(1, 5), rite="questioned", disposal="bench",
                                presumes="for", strikes=1, disposes="ban", quorum=None,
                                proofs=("testimony", "confession", "record"), bench_basis="determine"),
    "excommunication_deliberation": dict(authority="church", venue_min_rank="settlement", standard="hard",
                                         floor="closed", order="rank", exchanges=(1, 3), rite="contest",
                                         disposal="declared", presumes="for", strikes=0, disposes="ban", quorum=2,
                                         proofs=("record", "testimony"), bench_basis="determine"),
    "parliamentary_debate": dict(authority="polity", venue_min_rank="duchy", standard="demanding", floor="open",
                                 order="rank", exchanges=(3, 5), rite="contest", disposal="bench", presumes="none",
                                 strikes=0, disposes="Record", quorum=None, proofs=(), bench_basis="determine"),
    "council_of_state": dict(authority="polity", venue_min_rank="duchy", standard="demanding", floor="closed",
                             order="rank", exchanges=(2, 3), rite="contest", disposal="bench", presumes="none",
                             strikes=0, disposes="Record", quorum=None, proofs=(), bench_basis="determine"),
}
for _rid, _row in ROWS.items():
    _row["id"] = _rid
    _row["reason_bias"] = REASON_BIAS_SHIPPED[_rid]   # dials.controls() zeroes it at build time
ROW_IDS = tuple(ROWS)

# RD C.6 item 3 case_rows (part2:216-223), ordered, first match
CASE_ROWS = (
    ({"authority": "church", "matter": "person"}, "inquisition_hearing"),
    ({"authority": "polity", "matter": "proposition", "seat_at_least": "duchy"}, "parliamentary_debate"),
    ({"authority": "polity", "matter": "person", "bench": "several"}, "legal_trial"),
    ({"authority": "parties"}, "arbitration"),
    ({"matter": "record"}, "audience"),
    ({}, "arbitration"),
)
# rung kinds, in order (for venue_min_rank / seat_at_least). [ASSUMPTION G27: the tree's RUNG_KINDS order]
RUNG_KINDS = ("hearth", "settlement", "duchy", "realm")
DISPOSABLE_KINDS = ("oblige", "detain", "ban")   # [ASSUMPTION G27: `state/gate.py::DISPOSABLE_KINDS` not opened]

# B05.14 / B05.23 difficulty_ob: control arm 0/1/2/3, shipped (half arm) 0/0.5/1/1.5 (part8_cont.md:211)
DIFFICULTY_OB_SHIPPED = {"plain": 0.0, "routine": 0.5, "demanding": 1.0, "hard": 1.5}
# RD B.5 standard_demand (RD:810): control every level 0; shipped plain 0, routine 3, demanding 4, hard 5
STANDARD_DEMAND_SHIPPED = {"plain": 0.0, "routine": 3.0, "demanding": 4.0, "hard": 5.0}
STANDARD_DEMAND_CONTROL = {k: 0.0 for k in STANDARD_DEMAND_SHIPPED}
# B05.21 stakes_ob: control 0 for every kind; B98's first values (not shipped by B24p): oblige 0, detain .5, ban 1
STAKES_OB_CONTROL = {"oblige": 0.0, "detain": 0.0, "ban": 0.0, "none": 0.0, "Record": 0.0}
STAKES_OB_B98 = {"oblige": 0.0, "detain": 0.5, "ban": 1.0, "none": 0.0, "Record": 0.0}
