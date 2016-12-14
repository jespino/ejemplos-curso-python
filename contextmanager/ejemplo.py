from contextlib import contextmanager
import logging

@contextmanager
def logger():
    logging.warn("Entrando")
    yield 3
    logging.warn("Saliendo")

with logger() as dato:
    print dato


with transaction() as tx:
    cosas dentro de la transacion

with cd("/home/projecto"):
    haces cosas en ese directorio

# print "HOLA"
#
# class CTX(object):
#     def __enter__(self):
#         logging.warn("Entrando")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         logging.warn("Saliendo")
#         return True
#
# with CTX():
#     raise Exception("HOLA")
