import json,sys,collections
recs=json.load(open('recs.json'))
mine=set('personnel-roster npc-social cross-scale-plumbing resolution-kernel mass-battle-seam social-contest fieldwork-investigation'.split())
sel=[r for r in recs if r.get('system')==sys.argv[1]]
print(len(sel))
for r in sel:
    t=r.get('touches') or []
    if isinstance(t,str): t=[t]
    print(f"[{r.get('id')}] {r.get('slice')}/{r.get('status')} | {r.get('name')}")
    print(f"   src: {r.get('source')}  ev: {r.get('status_evidence','-')}  rolls:{r.get('rolls','-')} shape:{r.get('shape','-')} touches:{t} base:{r.get('baseline_ref','-')} conf:{r.get('conflicts_with','-')}")
    st=(r.get('statement') or '').replace('\n',' ')
    print(f"   {st}")
    if r.get('formula'): print(f"   FORMULA: {r['formula']}")
    print()
