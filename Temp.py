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


def func3(a):
    g = int(input('Число: '))
    b = []
    for i in a:
        c = i * g
        b.append(c)
    return b, a


def func4():
    print('asd')
