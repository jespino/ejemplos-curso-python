class A(object):
    pass


class B(object):
    pass


class C(A):
    pass


class MiClase(C, B):
    pass


print MiClase.mro()
