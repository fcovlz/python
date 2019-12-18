
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


a = fibonacci
print(a.next)
