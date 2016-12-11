class PrimeraCentena(object):
    def __contains__(self, obj):
        if isinstance(obj, int):
            return obj <= 100
        return False


valor = PrimeraCentena()
print 10 in valor
print 101 in valor
print "hola" in valor
