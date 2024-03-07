# https://docs.python.org/3/library/functions.html#filter
# https://www.w3schools.com/python/python_lists_comprehension.asp
def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    if (function is not None):
        return (item for item in iterable if function(item))

    return (item for item in iterable if item)
