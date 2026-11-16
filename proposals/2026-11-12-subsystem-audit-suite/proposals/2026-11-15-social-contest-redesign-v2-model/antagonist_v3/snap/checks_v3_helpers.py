from sc2.engine import Choice
def force(pred):
    def f(v, me):
        os_ = [o for o in v.options if pred(o)] or list(v.options)
        o = max(os_, key=lambda o: o.ev); return Choice(o.move, o.ground, o.item, o.relation)
    return f
only = lambda mv: force(lambda o: o.move == mv)
