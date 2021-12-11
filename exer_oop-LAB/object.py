class object :
    pass
class x(object):
    pass
class y(object):
    pass
class z (object):
    pass
class a(x):
    pass
class a(y):
    pass
class b(y):
    pass
class b(z):
    pass
class m(a,b):
    pass
class m(z):
    pass
