"""P8 -- is any threadwork code loaded by a season run? Builds the realm, runs ONE season through the
storybar composition, then lists sys.modules entries whose name contains 'thread' (excluding Python's
own `threading`/`_thread`) and every verb row whose name contains 'thread' with its executed count.
  PYTHONHASHSEED=0 python3 probes/p8_thread_import.py
"""
import sys
sys.path.insert(0, "/home/user/ttrpg")
from collections import Counter
from engine.season.harness import storybar as SB
from engine.season.data.verbs import VERB_TABLE
w, d, b = SB.drive(0, 1, "off", None)
mods = sorted(m for m in sys.modules if "thread" in m.lower() and m not in ("threading", "_thread", "_threading_local"))
print("modules loaded with 'thread' in name:", mods)
print("verb rows with 'thread':", [v for v in VERB_TABLE if "thread" in v])
k = Counter(e.kind for e in w.log)
print("thread-ish event kinds:", {kk: n for kk, n in k.items() if "thread" in kk or "lattice" in kk or "calamit" in kk})
print("log", len(w.log), "hash", w.content_hash()[:12])
