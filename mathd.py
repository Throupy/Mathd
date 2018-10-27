def fib(terms):
    """Return fibonacci sequence up to the number given"""
    results = []
    a, b = 0, 1
    for x in range(0, terms):
        i = a + b
        b, a = a, a + b
        results.append(i)
    return results


def tri_nums(terms):
    """Return triangle numbers up to the number given"""
    numbers = []
    a = 0
    for x in range(1, terms + 1):
        a += x
        numbers.append(a)
    return numbers


def square_nums(terms):
    numbers = []
    for x in range(1, terms + 1):
        numbers.append(x * x)
    return numbers


def linear_seq(sequence, term):
    """Finds the term given in any given linear sequence (same difference each time)"""
    if len(sequence) < 2:
        raise ValueError("Sequence must have at least 2 terms")
    n = sequence[1] - sequence[0]
    for x in range(0, len(sequence)):
        try:
            if sequence[x + 1] - sequence[x] != n:
                raise ValueError("Sequence is not linear")
        except IndexError:
            pass

    for x in range(1, len(sequence) + 1):
        plus = sequence[x - 1] - n * x

    return n * term + plus


def quadr_seq(sequence, term=10, return_nth=False):
    """Find the value of any given term in any given quadratic sequence"""
    if len(sequence) < 3:
        raise ValueError("Sequence must have at least 3 terms")
    difference = sequence[1] - sequence[0]
    second_difference = []
    third_difference = []
    for x in range(0, len(sequence)):
        try:
            second_difference.append(sequence[x + 1] - sequence[x])
        except IndexError:
            pass

    for x in range(0, len(second_difference)):
        try:
            third_difference.append(second_difference[x + 1] - second_difference[x])
        except IndexError:
            pass

    """
    nth term of quadratic sequence is always in form:
    an²+bn+c
    2a = 2nd differance(always constant)
    3a+b = 2nd term - 1st term
    a+b+c = 1st term
    using these rules I can calculate a, b and c.
    """
    if third_difference[1:] != third_difference[:-1]:
        raise ValueError("Sequence is not quadratic!")
    a = int(third_difference[0] / 2)
    b = 3 * a
    b = int(second_difference[0] - b)
    c = int(sequence[0] - a - b)

    n_sqrd = term * term
    if return_nth == True:
        if b >= 0:
            b = f"+{b}"
        if c >= 0:
            c = f"+{c}"
        return f"{a}n²{b}n{c}"
    else:
        return (a * n_sqrd) + (b * term) + c
