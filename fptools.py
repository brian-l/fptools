import types

from itertools import izip

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
    for val in izip(*lists):
        yield func(*val)

"""
Cycle through the values of _list forever
"""
def cycle(_list):
    while True:
        for item in _list:
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
Partition an iterable _list into a list of lists, each of
length 0-size
"""
def partition(_list, size):
    for item, pos in izip(_list, count(0, size)):
        items = _list[pos:pos + size]
        if items:
            yield items
        else:
            break

"""
Yield the first element as a single element list or empty list
"""
def head(_list):
    return next(iter(_list))

"""
Yield 2nd element and beyond
"""
def tail(_list):
    items = iter(_list)
    next(items)
    for item in items:
        yield item

"""
Yield everything except the last element
"""
def init(_list):
    raise NotImplementedError

"""
Return the last item.
"""
def last(_list):
    lt = None
    for item in _list:
        lt = item
    return lt

"""
Obligatory recursive fibonacci
"""
def fibonacci(count, _current=0, _next=1):
    if count <= 1:
        yield _current
    else:
        yield fibonacci(count - 1, _next, _current + _next)

"""
The Trampoline pattern. Takes a generator that yields itself from next()
Allows recursive algorithms without exceeding max recursion depth.
"""
def trampoline(gen, *args, **kwargs):
    func = gen(*args, **kwargs)
    while isinstance(func, types.GeneratorType):
        try:
            func = func.next()
        except StopIteration:
            break
    return func

"""
Recursive dictionary traversal
"""
def traverse(root, callback):
    callback(k, v)
    for k, v in root.items():
        if isinstance(v, dict):
            yield traverse(v, callback)
        else:
            callback(k, v)

if __name__ == '__main__':
    _list1 = [1,2,3,4,5]
    _list2 = [4,5,6]
    _list3 = [7,8,9]


