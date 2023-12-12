def add(*args):
    result = 0
    for arg in args:
        result += int(arg)
    return result


print(add(2, 3, 4, 5, 5, 7))
