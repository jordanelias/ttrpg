"""Which shipped role moves the abridged-conversation centre: shipped with one group returned to control.
usage: PYTHONHASHSEED=0 python lane1/centre_decomp.py [n]"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sitting, base_people, CARRIED
from scmodel import dials
N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
C = dials.controls()
GROUPS = {
    "none (shipped)": [],
    "fit": ["fit_level", "misfit_level"],
    "focus off_topic": ["off_topic_step"],
    "room (audience_room)": ["audience_room"],
    "blend tables": ["content_w_reason", "reason_bias"],
    "delivery/heard": ["delivery_step", "heard_step", "heard_floor"],
    "proofs cap": ["proofs_per_reason"],
    "will shield/resist": ["shield_step", "resist_step"],
    "grace standard/respect": ["standard_step", "respect_step"],
}
pp = base_people(rank=0, proofs=0.0, known=False)
for g, keys in GROUPS.items():
    D = dials.shipped(**{k: C[k] for k in keys})
    c = sum(sitting("private_abr", pp, D, ("dec", i))[2] in CARRIED for i in range(N)) / N
    print(f"shipped less {g:24} carried={c:.3f}±{math.sqrt(c*(1-c)/N):.3f}")
