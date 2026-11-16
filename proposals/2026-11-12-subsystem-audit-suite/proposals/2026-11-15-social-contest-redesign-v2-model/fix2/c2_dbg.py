from common import *
N=400
for lab,pol in (("argue",only("argue")),("rest",only("rest"))):
    own=defaultdict(list); fin=[]
    for i in range(N):
        inp,card,out,b=sit(mp,"questioning",M,("d",i),effort=3,deciders={"b":pol})
        for be in out.beats:
            for h,d in be.moved:
                if h=="b": own[(be.mover,be.move,be.relation,be.evaded)].append(d)
        fin.append(dict(out.state.tracks)["b"])
    print(lab, "final b track mean", round(sum(fin)/N,2), {k:(len(v),round(sum(v)/len(v),2)) for k,v in own.items()})
