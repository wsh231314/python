def cal(a):
    if not isinstance(a, (int, float)):
        raise TypeError("type error")
    return a * a


def array(arraylist):
    result = 0.0
    for val in arraylist:
        result = result + cal(val)
    return result

print(array([1, 2, 3, 5]))
