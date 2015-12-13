from collections import deque
from types import GeneratorType
try:
    from itertools import izip
    _range = xrange
    _zip = izip
except ImportError:
    # python 3, zip is lazy by default
    _zip = zip
    _range = range

def zip_with(func, *lists):
    """
    Zip n iterables into one list, calling func on the lists as a tuple
    """
    for val in _zip(*lists):
        yield func(*val)

def cycle(lst):
    """
    Cycle through the values of lst forever
    """
    while True:
        for item in iter(lst):
            yield item

def repeat(val):
    """
    Repeat val forever
    """
    while True:
        yield val

def repeat_fn(func, *args, **kwargs):
    """
    Repeat func() forever with optional arguments.
    """
    while True:
        yield func(*args, **kwargs)

def count(start=0, step=1):
    """
    Count from start by step forever
    """
    now = start
    while True:
        yield now
        now = now + step

def advance(i, n=1):
    """
    Try to advance the iterator i n number of times.
    """
    for x in _range(n):
        try:
            yield next(i)
        except StopIteration:
            return

def partition(itr, size):
    """
    Partition an iterable lst into a list of lists, each of
    length 0-size without slicing,
    to support generators which can't be sliced.
    """
    lst = iter(itr)
    while True:
        items = list(advance(lst, size))
        chunk = len(items)
        if chunk == size or chunk:
            yield items
        else:
            return

def unzip(*lists):
    """
    Reverse of izip.

    zip is its own inverse :)
    """
    return _zip(*lists)

def head(lst):
    """
    Yield the first element as a single element list or empty list
    """
    return next(iter(lst))

def tail(lst):
    """
    Yield 2nd element and beyond
    """
    items = iter(lst)
    next(items)
    for item in items:
        yield item

def init(lst):
    """
    Yield everything except the last element.

    While this can be done without slicing, it still requires full iteration of the sequence.
    The usefulness and performance of this function can be debated.
    """
    gen = iter(lst)
    q = deque()

    while True:
        try:
            q.append(next(gen))
            if len(q) > 2:
                yield q.popleft()
        except StopIteration:
            if len(q) > 1:
                yield q.popleft()
            return

def last(lst):
    """
    Return the last item.
    """
    lt = None
    for item in iter(lst):
        lt = item
    return lt

def trampoline(func, *args, **kwargs):
    """
    The Trampoline pattern. Takes a generator that yields itself from next()
    Allows recursive algorithms without exceeding max recursion depth.
    """
    gen = func(*args, **kwargs)
    try:
        while isinstance(gen, GeneratorType):
            gen = next(gen)
    except StopIteration:
        pass
    return gen

def gcd(a, b):
    """
    Recursive Euclid's algorithm for finding GCD
    """
    def _gcd(a, b):
        if b == 0:
            yield a
        else:
            yield gcd(b, a % b)
    return trampoline(_gcd, a, b)

def fibonacci(num):
    """
    Recursive fibonacci
    """
    def _fib(count, crnt=0, nxt=1):
        if count <= 1:
            yield crnt
        else:
            yield _fib(count - 1, nxt, crnt + nxt)
    return trampoline(_fib, num)

def factorial(num):
    """
    Recursive factorial
    """
    def _fact(c, n=1):
        if c <= 0:
            yield n
        else:
            yield _fact(c - 1, n * c)
    return trampoline(_fact, num)

