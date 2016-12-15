import time

def prueba():
    time.sleep(0.5)
    a = [1] * (10 ** 6)
    time.sleep(0.5)
    b = [2] * (2 * 10 ** 7)
    time.sleep(0.5)
    del b
    time.sleep(0.5)
    return a

if __name__ == "__main__":
    prueba()
