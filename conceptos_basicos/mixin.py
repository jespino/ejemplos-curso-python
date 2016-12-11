import logging


class Loggable(object):
    def log(self):
        logging.warn(str(self))


class MiClase(Loggable):
    pass

instancia = MiClase()
instancia.log()
