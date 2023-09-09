import random


def random_list():
    lst = []
    for i in range(20):
        lst.append(random.randint(1, 100))
    return lst
