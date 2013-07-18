from itertools import chain
from functools import partial

def shortest(lists):
    return min(lists, key=len)

def zipWith(func, *lists):
    for val in zip(lists):
        yield func(chain(*val))

def cycle(lst):
    while True:
        for item in lst:
            yield item

def repeat(val):
    while True:
        yield val

if __name__ == '__main__':
    lst1 = [1,2,3,4,5]
    lst2 = [4,5,6]
    lst3 = [7,8,9]

    for z in zipWith(sum, lst1, lst2, cycle(3)):
        print z
