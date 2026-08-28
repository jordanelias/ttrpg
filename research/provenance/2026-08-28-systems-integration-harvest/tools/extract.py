import re, sys, yaml, glob, os, json
d = "/tmp/claude-0/-home-user-ttrpg/d10fce8e-35f0-503e-88b1-0cc6361eac31/scratchpad/run/records"
out = []
def manual(chunk):
    r = {}
    key=None; buf=[]
    for line in chunk.split("\n"):
        m = re.match(r"^\s{0,4}-?\s*([a-z_]+):\s?(.*)$", line)
        if m and (line.startswith("- ") or re.match(r"^  [a-z_]+:", line)):
            if key: r[key]="\n".join(buf).strip()
            key=m.group(1); buf=[m.group(2)]
        else:
            buf.append(line.strip())
    if key: r[key]="\n".join(buf).strip()
    for k,v in list(r.items()):
        if isinstance(v,str):
            v=v.strip()
            if v.startswith(">-") or v.startswith("|"): v=v[2:].strip()
            r[k]=re.sub(r"\s+"," ",v).strip().strip('"')
    return r
for f in sorted(glob.glob(d+"/*.md")):
    txt = open(f).read()
    blocks = re.findall(r"```yaml\n(.*?)```", txt, re.S)
    for b in blocks:
        chunks = re.split(r"\n(?=- id:)", "\n"+b.strip())
        for c in chunks:
            c=c.strip()
            if not c.startswith("- id:"): continue
            rec=None
            try:
                p = yaml.safe_load(c)
                if isinstance(p, list) and len(p)==1 and isinstance(p[0], dict): rec=p[0]
            except Exception: pass
            if rec is None: rec = manual(c)
            rec['_lane']=os.path.basename(f)[:-3]
            out.append(rec)
print(len(out), file=sys.stderr)
json.dump(out, open("all.json","w"), indent=1)
from collections import Counter
print(Counter(r.get('system') for r in out), file=sys.stderr)
