import os,re,subprocess
SUP="proposals/2026-08-31-ideal/10_SUPERSEDING.md"
REV="proposals/2026-08-31-ideal/20_FABLE5_ADVERSARIAL_REVIEW.md"
V2D="proposals/2026-08-31-ideal-v2"
surfaces={}
surfaces['SUP']=open(SUP,encoding='utf8').read()
surfaces['REV']=open(REV,encoding='utf8').read()
surfaces['v2']="".join(open(os.path.join(V2D,f),encoding='utf8').read() for f in sorted(os.listdir(V2D)) if f.endswith('.md') and not f.startswith('04_'))
ref={SUP,REV}|{os.path.join(V2D,f) for f in os.listdir(V2D) if f.endswith('.md')}
docs=[]
for r,d,fs in os.walk('proposals'):
    for f in fs:
        if not f.endswith('.md'): continue
        p=os.path.join(r,f)
        n=sum(1 for _ in open(p,encoding='utf8',errors='replace'))
        docs.append((p,n))
over=[(p,n) for p,n in docs if n>200]
print("all md in proposals:",len(docs))
print(">200 lines:",len(over))
print("of those, reference surfaces:",sum(1 for p,n in over if p in ref))
swept=[(p,n) for p,n in over if p not in ref]
print("swept:",len(swept))
SUITE="proposals/2026-08-29-valoria-from-scratch/"
uncited=[];cited=[]
for p,n in swept:
    b=os.path.basename(p)
    tot={}
    for k,txt in surfaces.items():
        c=txt.count(p)+txt.count(b)
        if p.startswith(SUITE):
            m=re.match(r'(\d\d)_',b)
            if m: c+=len(re.findall(r'`'+m.group(1)+r':[0-9]',txt))
        tot[k]=c
    (uncited if sum(tot.values())==0 else cited).append((p,n,tot))
print("CITED:",len(cited)," UNCITED:",len(uncited))
print("---- cited detail ----")
for p,n,t in sorted(cited,key=lambda x:-sum(x[2].values())):
    print(f"{sum(t.values()):5d}  SUP{t['SUP']:<4d} REV{t['REV']:<4d} v2{t['v2']:<5d} {n:5d}L  {p}")
