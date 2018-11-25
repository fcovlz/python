
def fibonacci_lineal0(end_number):
    a, b = 0, 1
    for index in range(end_number):
        a, b = b, a + b
    return a


def fibonacci_lineal1(end_number):
    a = 0
    b = 1
    for index in range(end_number):
        prev_a = a
        a = b
        b = prev_a + b
    return a


def fibonacci_lineal2(end_number):
    result = [0, 1]
    for index in range(end_number):
        result.append(result[-1] + result[-2])

    return result[-2:-1][0]


def fibonacci_yield():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


def fibonacci_recursive0(end_number):
    if end_number < 2:
        return end_number
    return fibonacci_recursive0(end_number-2) + \
        fibonacci_recursive0(end_number-1)


def fibonacci_recursive1(end_number):
    if end_number == 2 or end_number == 1 :
        return 1
    else:
        return fibonacci_recursive1(end_number-1) + \
               fibonacci_recursive1(end_number-2)


if __name__ == "__main__":
    end_number = 10

    result = fibonacci_lineal0(end_number)
    print result

    result = fibonacci_lineal1(end_number)
    print result

    result = fibonacci_lineal2(end_number)
    print result

    result = fibonacci_recursive0(end_number)
    print result

    a = fibonacci_yield()
    print a.next()
    print a.next()
    print a.next()

    result = fibonacci_recursive1(end_number)
    print result
