import time
import cProfile

def prueba():
    return 2 + 2

def prueba2():
    return 3 + 3

def prueba_larga():
    time.sleep(2)

def all():
    prueba()
    prueba2()
    prueba_larga()

all()
