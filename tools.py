from itertools import chain, izip

"""
A small module with functions based on idioms I learned
while programming Haskell and other languages.

"""

"""
Return the size of the shortest list in a list of lists
"""
def shortest(lists):
    return min(lists, key=len)

"""
Zip n iterables into one list, calling func on the lists as a tuple
"""
def zipWith(func, *lists):
    for val in izip(lists):
        yield func(chain(*val))

"""
Cycle through the values of lst forever
"""
def cycle(lst):
    while True:
        for item in lst:
            yield item

"""
Repeat val forever
"""
def repeat(val):
    while True:
        yield val

"""
Count from start by step forever
"""
def count(start=0, step=1):
    now = 0
    while True:
        yield now
        now = now + start + step

"""
Partition an iterable lst into a list of lists, each of
length 0-size
"""
def partition(lst, size):
    for item, pos in izip(lst, count(0, size)):
        items = lst[pos:pos + size]
        if items:
            yield items
        else:
            break

if __name__ == '__main__':
    lst1 = [1,2,3,4,5]
    lst2 = [4,5,6]
    lst3 = [7,8,9]

    print [p for p in partition([1,2,3,4,5,6,7,8,9,10], 3)]

