class Singleton(type):
    instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance

class A(object):
    pass

class B(object):
    __metaclass__ = Singleton

a1 = A()
a2 = A()
print a1 is a2

b1 = B()
b2 = B()
print b1 is b2
