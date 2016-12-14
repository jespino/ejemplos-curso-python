def fib():
    num1 = 1
    num2 = 1
    yield num1
    yield num2
    while True:
        aux = num2
        num2 = num1 + num2
        num1 = aux
        yield num2

for x in fib():
    if x < 50:
        print x
    else:
        break

var = fib()
for x in range(10):
    y = var.next()
    print y
