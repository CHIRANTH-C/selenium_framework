def factorial_func(num):
    assert num >= 0. and type(num) is int, "Invalid input , input must be positive integer"
    if num == 0:
        return 1
    else:
        result = num * factorial_func(num-1)
        # print(type(result))
        return result