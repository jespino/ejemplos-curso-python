class Potencia(object):
    def __init__(self, potencia):
        self._potencia = potencia

    def __call__(self, value):
        return value ** self._potencia

cuadrado = Potencia(2)
cubo = Potencia(3)

print cuadrado(3)
print cubo(3)
