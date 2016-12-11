from repoze.lru import lru_cache
from types import FunctionType
import time

class Cache(type):
    def __init__(cls, name, bases, namespace):
        for key, value in namespace.items():
            if isinstance(value, FunctionType):
                setattr(cls, key, lru_cache(maxsize=500)(value))

        return super(Cache, cls).__init__(name, bases, namespace)

class A(object):
    __metaclass__ = Cache

    def calc(self):
        time.sleep(2) # Calculo pesado
        return "HOLA"

a = A()
print "Principio"
print a.calc()
print "Medio"
print a.calc()
print "Final"
