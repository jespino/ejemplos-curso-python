import logging

class Logger(object):
    def __init__(self, *args, **kwargs):
        super(Logger, self).__init__(*args, **kwargs)
        logging.warn(str(self))

class Countable(object):
    _count = 0

    def count(self):
        return self._count

    def inccount(self):
        self._count += 1


class MiClase(Logger, Countable):
    pass


x = MiClase()
y = MiClase()

x.inccount()
x.inccount()
x.inccount()
x.inccount()
print x.count()
print y.count()

print MiClase.mro()
