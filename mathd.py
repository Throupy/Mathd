import itertools

def fib(terms):
    """Return fibonacci sequence up to the number given"""
    if terms < 1:
        raise ValueError("Must choose at least 1 term")
    results = []
    a, b = 0, 1 #Set up constants
    for x in range(0, terms):
        i = a + b #Create a new constant, equal to the sum of the 2 prev constants
        b, a = a, a + b #set b to a and a to a + b
        results.append(i) #add the result to the list (this will be the actual fib number to be returned)
    return results


def tri_nums(terms):
    """Return triangle numbers up to the number given"""
    if terms < 1:
        raise ValueError("Must choose at least 1 term")
    numbers = []
    a = 0
    for x in range(1, terms + 1):
        a += x
        numbers.append(a)
    return numbers


def square_nums(terms):
    if terms < 1:
        raise ValueError("Must choose at least 1 term")
    numbers = []
    for x in range(1, terms + 1):
        numbers.append(x * x)
    return numbers


def linear_seq(sequence, term):
    """Finds the term given in any given linear / arithmetic sequence (same difference each time)"""
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


def lcm(x, y):
    """Return the lowest common mutliple of two numbers given"""
    if x == 0 or y == 0:
        raise ValueError("Values can not be 0")
    greater = y
    if x > y:
        greater = x
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

def hcf(x, y):
    """Return the highest common factor of two given numbers"""
    if x == 0 or y == 0 or not isinstance(x, int) or not isinstance(x, int):
        raise ValueError("Values can not be 0 or non-integers")
    xfactors = []
    yfactors = []
    for a,b in zip(range(1,int(x+1)), range(1,int(y+1))):
        if float(x/a).is_integer():
            xfactors.append(x/a)
        if float(y/b).is_integer():
            yfactors.append(y/b)
    for factor in xfactors:
        if factor in yfactors:
            return int(factor)

def avg(data):
    """Returns the average value of a given data set"""
    if not all(isinstance(x, (int,float)) for x in data) or len(data) < 1:
        raise ValueError("All items in dataset must be integers or floats")
    return sum(data) / len(data)

def mode(data):
    """Returns the element with the most occurences in a data set, if one is not present it will return lowest"""
    if not all(isinstance(x, (int,float)) for x in data) or len(data) < 1:
        raise ValueError("All items in dataset must be integers or floats")
    return max(set(data), key=data.count)
