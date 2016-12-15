import timeit

valor = {"x": 2}

def try_except_positivo():
    try:
        return valor['x']
    except KeyError:
        return None

def try_except_negativo():
    try:
        return valor['y']
    except KeyError:
        return None

def if_positivo():
    if 'x' in valor:
        return valor['x']
    return None

def if_negativo():
    if 'y' in valor:
        return valor['y']
    return None

if __name__ == "__main__":
    setup_expr = "from try_except import *"
    print "Try-except positivo: ", timeit.timeit("try_except_positivo()", setup=setup_expr)
    print "Try-except negativo: ", timeit.timeit("try_except_negativo()", setup=setup_expr)
    print "If positivo: ", timeit.timeit("if_positivo()", setup=setup_expr)
    print "If negativo", timeit.timeit("if_negativo()", setup=setup_expr)
