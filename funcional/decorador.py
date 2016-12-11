import logging
from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = "func: %s, args: %s, kwargs: %s" % (func.__name__, str(args), str(kwargs))
        logging.warn(text)
        return_value = func(*args, **kwargs)
        text = "func: %s, return_value: %s" % (func.__name__, str(return_value))
        logging.warn(text)
        return return_value

    return wrapper


@logger
def suma(x, y):
    return x + y


suma(3,5)
