from time import sleep


def repeat(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            if i > 0:
                sleep(2)
            print('Args:', ', '.join([*[str(arg) for arg in args],
                                      *[f'{arg}={kwargs[arg]}' for arg in kwargs]]))
            print('Result:', func(*args, **kwargs))
    return wrapper


@repeat
def foo(a, b, c):
    print('[foo]')
    return a + b + c


foo(1, 2, c=3)
