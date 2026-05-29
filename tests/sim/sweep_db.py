import sys, os, random, statistics
exec(open('/home/claude/sim_v22_db.py').read())
ANCHOR={('Line',3):9,('Arrowhead',3):8,('Horseshoe',3):8,('GappedLine',3):7,('RefusedFlank',3):9}
def mk(shape,name,fac):
    ad=-1 if fac=='A' else 1; sr=SIDE_A_START_ROW if fac=='A' else SIDE_B_START_ROW
    su=Subunit(shape=shape,troop_type='infantry',tier=3,starting_position=(sr,ANCHOR[(shape,3)]),advance_dir=ad,unit_type='melee')
    return Unit(name=name,faction=fac,power=4,command=4,discipline=5,discipline_start=5,morale=6,morale_start=6,subunits=[su],dr=1,stance='balanced')
M=[('H1','Line','Line',45,55),('H2','Arrowhead','Line',50,65),('H3','Horseshoe','Line',50,65),
   ('H4','Horseshoe','Arrowhead',40,60),('H5','RefusedFlank','Horseshoe',50,65),('H6','RefusedFlank','Line',45,60),
   ('H7','GappedLine','Line',50,65),('H8','GappedLine','Arrowhead',45,60),('H9','Line','Arrowhead',35,50),
   ('H10','Line','Horseshoe',35,50),('H11','Arrowhead','Horseshoe',40,60)]
def run(sa,sb,n=40):
    aw=bw=0;ca=[];cb=[]
    for s in range(n):
        random.seed(s+1000000); ua=mk(sa,'A','A'); ub=mk(sb,'B','B'); a0,b0=ua.hp_max,ub.hp_max
        r=run_multi_turn_battle(ua,ub,sa,sb,ANCHOR,max_battle_turns=20)
        if r['winner']=='A':aw+=1
        elif r['winner']=='B':bw+=1
        ca.append(100*(a0-ua.hp)/a0); cb.append(100*(b0-ub.hp)/b0)
    return aw/n*100, statistics.mean(ca), statistics.mean(cb)
cs=os.environ.get('CASUALTY_SCALE')
nb=0; h1cas=None; h4=None
for tid,sa,sb,lo,hi in M:
    a,ca,cb=run(sa,sb)
    if lo<=a<=hi: nb+=1
    if tid=='H1': h1cas=(ca+cb)/2
    if tid=='H4': h4=a
print(f"CASUALTY_SCALE={cs:>4}  H1_mirror_cas={h1cas:5.1f}%  in-band={nb}/11  H4_Cannae_Awin={h4:5.1f}%")
