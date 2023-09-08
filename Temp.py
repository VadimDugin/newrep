from main import random_list


def func(a):
    b = 0
    for i in a:
        b += i
    return b


def func2(a):
    s = 1000000
    for i in a:
        s -= i
    return s


a = 100
print(random_list())
print(func2(random_list()))
