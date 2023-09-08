from main import random_list


def func(a):
    b = 0
    for i in a:
        b += i
    return b


print(random_list())
print(func(random_list()))
