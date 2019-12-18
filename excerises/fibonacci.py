def fibonacci_lineal0(end_number):
    a, b = 0, 1
    for index in range(end_number):
        a, b = b, a + b
    return a
