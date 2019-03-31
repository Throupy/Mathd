"""Mathd module."""


class Mathd:
    """Mathd class."""

    @staticmethod
    def fib(terms: list = []):
        """Return fibonacci sequence up to the number given."""
        if terms < 1:
            raise ValueError("Must choose at least 1 term")
        results = []
        a, b = 0, 1
        for x in range(0, terms):
            i = a + b
            b, a = a, a + b
            results.append(i)
        return results

    @staticmethod
    def tri_nums(terms: list = []):
        """Return triangle numbers up to the number given."""
        if terms < 1:
            raise ValueError("Must choose at least 1 term")
        numbers = []
        a = 0
        for x in range(1, terms + 1):
            a += x
            numbers.append(a)
        return numbers

    @staticmethod
    def square_nums(terms: list = []):
        """Return square numbers up to the number given."""
        if terms < 1:
            raise ValueError("Must choose at least 1 term")
        numbers = []
        for x in range(1, terms + 1):
            numbers.append(x * x)
        return numbers

    @staticmethod
    def linear_seq(sequence: int = 1, term: int = 1):
        """Find the term given in any given linear / arithmetic sequence."""
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

    @staticmethod
    def quadr_seq(seq: list = [], term: int = 10, return_nth: bool = False):
        """Find the value of any given term in any given quadratic sequence."""
        if len(seq) < 3:
            raise ValueError("Sequence must have at least 3 terms")
        second_difference = []
        third_difference = []
        for x in range(0, len(seq)):
            try:
                second_difference.append(seq[x + 1] - seq[x])
            except IndexError:
                pass

        for x in range(0, len(second_difference)):
            try:
                third_difference.append(
                            second_difference[x + 1] - second_difference[x]
                                        )
            except IndexError:
                pass

        if third_difference[1:] != third_difference[:-1]:
            raise ValueError("Sequence is not quadratic!")
        a = int(third_difference[0] / 2)
        b = 3 * a
        b = int(second_difference[0] - b)
        c = int(seq[0] - a - b)

        n_sqrd = term * term
        if return_nth is True:
            if b >= 0:
                b = f"+{b}"
            if c >= 0:
                c = f"+{c}"
            return f"{a}n²{b}n{c}"
        else:
            return (a * n_sqrd) + (b * term) + c

    @staticmethod
    def lcm(x: int = 0, y: int = 0):
        """Return the lowest common mutliple of two numbers given."""
        if x == 0 or y == 0:
            raise ValueError("Values can not be 0")
        greater = y
        if x > y:
            greater = x
        while True:
            if greater % x == 0 and greater % y == 0:
                return greater
            greater += 1

    @staticmethod
    def hcf(x, y):
        """Return the highest common factor of two given numbers."""
        if x == 0 or y == 0 or \
           not isinstance(x, int) or not isinstance(x, int):
            raise ValueError("Values can not be 0 or non-integers")
        xfactors = []
        yfactors = []
        for a, b in zip(range(1, int(x+1)), range(1, int(y+1))):
            if float(x/a).is_integer():
                xfactors.append(x/a)
            if float(y/b).is_integer():
                yfactors.append(y/b)
        for factor in xfactors:
            if factor in yfactors:
                return int(factor)

    @staticmethod
    def gradient(points: list = []):
        """Find the gradient of a line given any 2 or more points.

        Arguments:
            Points - list of tuples containing x and y values (x,y)
        """
        if len(points) < 1:
            raise ValueError("You must specify some points, format (x,y)")
        gradient = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
        return gradient

    def findYIntercept(self, points: list = []):
        """Find the y intercept of a line given any 2 or more points.

        Arguments:
            Points - list of tuples containing x and y values (x,y)
        """
        gradient = self.gradient(points)
        point = points[0]
        # Set up y = mx + b equation and solve for b
        b = point[1] - (gradient*point[0])
        return b

    def lineEquation(self, points: list = []):
        """Find the equation of a line given any 2 or more points.

        Arguments:
            Points - list of tuples containing x and y values (x,y)
        """
        gradient = self.gradient(points)
        intercept = self.findYIntercept(points)
        equation = f'y={gradient}x+{intercept}'
        return equation

    @staticmethod
    def avg(data):
        """Return the average value of a given data set."""
        if not all(isinstance(x, (int, float)) for x in data) or len(data) < 1:
            raise ValueError("All items in dataset must be integers or floats")
        return sum(data) / len(data)

    @staticmethod
    def mode(data):
        """Return the element with the most occurences in a data set."""
        if not all(isinstance(x, (int, float)) for x in data) or len(data) < 1:
            raise ValueError("All items in dataset must be integers or floats")
        return max(set(data), key=data.count)
