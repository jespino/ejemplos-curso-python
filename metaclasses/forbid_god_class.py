from types import FunctionType


class ForbidGodClass(type):
    def __init__(cls, name, bases, namespace):
        if len(filter(lambda x: isinstance(x, FunctionType), namespace.values())) > 5:
            raise Exception("Too much methods")
        super(ForbidGodClass, cls).__init__(name, bases, namespace)
    def __setattr__(cls, name, value):
        if isinstance(value, FunctionType):
            raise Exception("You can't assign new methods")
        super(ForbidGodClass, cls).__setattr__(name, value)


class A(object):
    __metaclass__ = ForbidGodClass

    def a():
        pass
    def b():
        pass
    def c():
        pass
    def d():
        pass
    def e():
        pass

A.f = lambda x: 123
