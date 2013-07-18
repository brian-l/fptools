from itertools import chain

"""
Return the size of the shortest list in a list of lists
"""
def shortest(lists):
    return min(lists, key=len)

"""
Zip n iterables into one list, calling func on the lists as a tuple
"""
def zipWith(func, *lists):
    for val in zip(lists):
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
    for pos in count(0, size):
        # yield lst[pos:pos + size]
        print pos

if __name__ == '__main__':
    lst1 = [1,2,3,4,5]
    lst2 = [4,5,6]
    lst3 = [7,8,9]

    # for x,y in zip(xrange(100), repeat(1)):
    #     print x,y
    print [p for p in partition([1,2,3,4,5,6,7,8,9], 3)]

