class Other(object):
    other = 0

    def __getattr__(self, name):
        if name in self.__dict__:
            return super(Other, self).__getattribute__(name)
        else:
            return super(Other, self).__getattribute__('other')

    def __setattr__(self, name, value):
        if name in self.__dict__:
            super(Other, self).__setattr__(name, value)
        else:
            super(Other, self).__setattr__('other', value)

instance = Other()
print(instance.uno)
instance.dos = 3
print(instance.tres)
