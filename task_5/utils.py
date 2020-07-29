from typing import List


def generate_fibonacci(n: int) -> List[int]:
    """
    This method generates the first n numbers of Fibonacci.
    :param n:
    :return: a list of the first n numbers of Fibonacci.
    """

    a = 0
    b = 1
    numbers = []
    if n == 1:
        numbers.append(a)
        return numbers

    numbers.extend([a, b])
    while n - 2:
        a, b = b, a + b
        numbers.append(b)
        n -= 1

    return numbers
