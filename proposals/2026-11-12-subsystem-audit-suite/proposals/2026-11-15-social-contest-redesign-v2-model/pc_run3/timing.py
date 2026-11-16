from common import *
for ctx in CTX:
    for kind in ("blank","rich"):
        pp = blank() if kind=="blank" else rich(); m = mat(kind)
        t=time.time(); n=40
        c=sum(sit(pp, ctx, m, ("t",i))[3][0] in CARRIED for i in range(n))
        print(ctx, kind, round((time.time()-t)/n*1000,1), "ms", c/n)
