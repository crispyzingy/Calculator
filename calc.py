def calc(f, x, y):
    return f(x, y)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


print(calc(add, 10, 20))
print(calc(sub, 20, 15))
