from types import GeneratorType
from itertools import izip

"""
Zip n iterables into one list, calling func on the lists as a tuple
"""
def zipWith(func, *lists):
    for val in izip(*lists):
        yield func(*val)

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

"""
Yield the first element as a single element list or empty list
"""
def head(lst):
    return next(iter(lst))

"""
Yield 2nd element and beyond
"""
def tail(lst):
    items = iter(lst)
    next(items)
    for item in items:
        yield item

"""
Yield everything except the last element

I haven't figured out how to do this yet
"""
def init(lst):
    raise NotImplementedError

"""
Return the last item.
"""
def last(lst):
    lt = None
    for item in lst:
        lt = item
    return lt

"""
The Trampoline pattern. Takes a generator that yields itself from next()
Allows recursive algorithms without exceeding max recursion depth.
"""
def trampoline(func, *args, **kwargs):
    gen = func(*args, **kwargs)
    try:
        while isinstance(gen, GeneratorType):
            gen = gen.next()
    except StopIteration:
        pass
    return gen

"""
Recursive Euclid's algorithm for finding GCD
"""
def gcd(a, b):
    if b == 0:
        yield a
    else:
        yield gcd(b, a % b)

def fib(count, crnt=0, nxt=1):
    if count <= 1:
        yield crnt
    else:
        yield fib(count - 1, nxt, crnt + nxt)

