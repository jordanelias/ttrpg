import json, sys, os, pathlib
T = "/tmp/claude-0/-home-user-ttrpg/78360267-ece4-57b1-8568-be13abd76bad/tasks"
OUT = "/tmp/claude-0/-home-user-ttrpg/78360267-ece4-57b1-8568-be13abd76bad/scratchpad/lanes"
MAP = {
 "a914b9e684311ea67":"FABLE1","a407991a38d4f5bbe":"FABLE2","a9e2268f1d0c2bc74":"FABLE3",
 "a1efd5bc0f2409008":"A","ab2074a2e5da5c0aa":"B","aeb3cb7743284f642":"C",
 "a0ebb56304b333103":"D","ad12b97a6f570a9be":"E","ad663be4d5705aad9":"F",
 "a9010ce822b9c7d36":"G","a5b6aeaaffdbc8e1c":"H","a1ec6d6e832b74c17":"I",
 "a9c8afdb08666edb7":"J","af989210f14dd59c4":"K","aac74ee71f55b0179":"L",
}
pathlib.Path(OUT).mkdir(parents=True, exist_ok=True)
for aid, lane in sorted(MAP.items(), key=lambda x: x[1]):
    p = os.path.join(T, aid + ".output")
    if not os.path.exists(p):
        print(f"{lane}: NO FILE"); continue
    last = None
    with open(p) as f:
        for line in f:
            line = line.strip()
            if not line: continue
            try: d = json.loads(line)
            except Exception: continue
            m = d.get("message")
            if not isinstance(m, dict): continue
            if m.get("role") != "assistant": continue
            c = m.get("content")
            txt = ""
            if isinstance(c, str): txt = c
            elif isinstance(c, list):
                txt = "\n".join(b.get("text","") for b in c
                                if isinstance(b, dict) and b.get("type")=="text")
            if txt.strip(): last = txt
    if last is None:
        print(f"{lane}: no assistant text yet"); continue
    dest = os.path.join(OUT, f"LANE_{lane}.md")
    with open(dest, "w") as g: g.write(last)
    print(f"{lane}: {len(last):>7} chars, {len(last.split()):>6} words -> LANE_{lane}.md")
