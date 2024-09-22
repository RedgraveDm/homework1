

def check_iterable(obj):
    if type(obj) is str and len(obj) == 1:
        return False
    try:
        iter(obj)
        return True
    except TypeError:
        return False


def flatten(iterable):
    for item in iterable:
        if check_iterable(item):
            yield from flatten(item)
        else:
            yield item


#test_obj = [[1, 2, 3], [4, [5, 6, [7, 8]]]]
test_obj = [1, 2, 'abc', [2, 4], {'key': 'value'}]
print(list(flatten(test_obj)))
