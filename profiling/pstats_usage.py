import time
import cProfile
import pstats

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

profiler = cProfile.Profile()
profiler.enable()
all()
profiler.disable()

stats = pstats.Stats(profiler)
stats.sort_stats("name") # Ordenamos por nombre de funcion
stats.print_stats('prueba', 2) # Filtramos por texto y limitamos las lineas a 2
print("-------------------------------")
stats.print_stats(2, 'prueba') # Que no es lo mismo que hacerlo al reves
print("-------------------------------")
stats.print_stats(0.5) # Puedo tambien pedir un porcentaje de las filas
