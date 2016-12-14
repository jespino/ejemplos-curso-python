from functools import wraps, partial

def duplicate(func):
    @wraps(func)
    def wrapper(x, y):
        resultado = func(x, y)
        return resultado * 2
    return wrapper

def multiplicar(func=None, n=1):
    if func is None:
        return partial(multiplicar, n=n)

    def wrapper(x, y):
        resultado = func(x, y)
        return resultado * n
    return wrapper

def suma(x, y):
    return x + y
suma_original = suma
suma = multiplicar(suman=3)()


print suma(2, 2)
