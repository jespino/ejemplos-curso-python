import time
from functools import partial

mayores_de_2 = partial(filter, lambda x: x > 2)

lista = [0, 1, 2, 3, 4]
print mayores_de_2(lista)
