import json, os, pathlib
T = "/tmp/claude-0/-home-user-ttrpg/78360267-ece4-57b1-8568-be13abd76bad/tasks"
OUT = "/tmp/claude-0/-home-user-ttrpg/78360267-ece4-57b1-8568-be13abd76bad/scratchpad/cases"
MAP = {
 "aa6be0c29808bfb5f":"NPC1","a1f823d2f8a68c388":"NPC2","a4a5fe863f4a7b0c3":"NPC3",
 "a9a113480210e8b12":"ARC1","a3021d1f566d089c8":"ARC2","af631707cc3acc4f8":"ARC3",
}
pathlib.Path(OUT).mkdir(parents=True, exist_ok=True)
for aid, lane in sorted(MAP.items(), key=lambda x: x[1]):
    p = os.path.join(T, aid + ".output")
    if not os.path.exists(p):
        print(f"{lane}: NO FILE"); continue
    last = None
    with open(p) as f:
        for line in f:
            line=line.strip()
            if not line: continue
            try: d=json.loads(line)
            except Exception: continue
            m=d.get("message")
            if not isinstance(m,dict) or m.get("role")!="assistant": continue
            c=m.get("content"); txt=""
            if isinstance(c,str): txt=c
            elif isinstance(c,list):
                txt="\n".join(b.get("text","") for b in c if isinstance(b,dict) and b.get("type")=="text")
            if txt.strip(): last=txt
    if last is None:
        print(f"{lane}: pending"); continue
    open(os.path.join(OUT,f"{lane}.yaml"),"w").write(last)
    print(f"{lane}: {len(last):>7} chars -> {lane}.yaml")
