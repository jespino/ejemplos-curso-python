def func(value):
    if isinstance(value, int):
        return value * 2
    elif isinstance(value, long):
        return value / 2
    return value

print func(10)
print func(10l)
print func("hola")
