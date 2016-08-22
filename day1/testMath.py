import math


def getresult(a, b, c):
    if not isinstance(a, int):
        raise TypeError('type error!!')

    return abs(a) + abs(b) + c

print(getresult('a', 2, 3))