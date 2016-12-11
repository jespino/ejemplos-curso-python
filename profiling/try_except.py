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
    print "Try-except positivo: ", timeit.timeit("try_except_positivo()", setup="from try_except import try_except_positivo")
    print "Try-except negativo: ", timeit.timeit("try_except_negativo()", setup="from try_except import try_except_negativo")
    print "If positivo: ", timeit.timeit("if_positivo()", setup="from try_except import if_positivo")
    print "If negativo", timeit.timeit("if_negativo()", setup="from try_except import if_negativo")
