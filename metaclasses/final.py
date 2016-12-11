class MetaFinal(type):
    def __init__(cls, name, bases, namespace):
        super(MetaFinal, cls).__init__(name, bases, namespace)
        for klass in bases:
            if isinstance(klass, MetaFinal):
                raise TypeError(str(klass.__name__) + " es final")


class A(object):
    __metaclass__ = MetaFinal

class B(A):
    pass
