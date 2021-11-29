'''
Example Decorators
'''
from functools import wraps
import time


key = False


# Basic decorator:
def decorate(func):
    def inner(*args, **kwargs):
        seplen = 50

        print('-' * seplen)
        print(f'Wrapped function {func}:')
        print(f'Positional arguments:  {args}')
        print(f'Keyword arguments:  {kwargs}')
        print('-' * seplen)
        print('Optional pre-processing...')
        print(f'Invoking {func} to capture return value(s)...')
        res = func(*args, **kwargs)
        print(f'Captured:  {res}')
        print('Optional post-processing...')
        print('-' * seplen)

        return res
    return inner


# Decorator with parameters (accepts arguments):
def decorateplus(*dargs, **dkwargs):
    def wrap(func):
        def wrapped(*wargs, **wkwargs):
            seplen = 50

            print('-' * seplen)
            print('Decorator arguments:')
            print(f'Positional:  {dargs}')
            print(f'Keyword:  {dkwargs}')
            print('-' * seplen)
            print(f'Wrapped function {func.__name__}:')
            print(f'Positional arguments:  {wargs}')
            print(f'Keyword arguments:  {wkwargs}')
            print('-' * seplen)
            print('Optional pre-processing...')
            print(f'Invoking {func.__name__} to capture return value(s)...')
            res = func(*wargs, **wkwargs)
            print(f'Captured:  {res}')
            print('Optional post-processing...')
            if dkwargs.get('modify') == True:
                print('Modifcation enabled - altering return value.')
                res *= wargs[0]
            print('-' * seplen)

            return res
        return wrapped
    return wrap


# Decorator with parameters (accepts arguments) and look like wrapped function:
def decoratepp(*dargs, **dkwargs):
    def wrap(func):
        # Make the wrapped function look like the original:
        # e.g., __module__, __name__, __qualname__, __annotations__, __doc__,
        # and __dict__ are copied from original function to wrapped function
        @wraps(func)
        def wrapped(*wargs, **wkwargs):
            seplen = 50

            print('-' * seplen)
            print('Decorator arguments:')
            print(f'Positional:  {dargs}')
            print(f'Keyword:  {dkwargs}')
            print('-' * seplen)
            print(f'Wrapped function {func.__name__}:')
            print(f'Positional arguments:  {wargs}')
            print(f'Keyword arguments:  {wkwargs}')
            print('-' * seplen)
            print('Pre-processing (tracking time)...')
            start_time = time.perf_counter()
            print(f'Invoking {func.__name__} to capture return value(s)...')
            res = func(*wargs, **wkwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            print(f'Captured:  {res}')
            print('Post-processing (tracking time)...')
            print(f'{func.__name__!r} ran in {run_time:.6f} seconds')
            if dkwargs.get('modify') == True:
                print('Modifcation enabled - altering return value.')
                res *= wargs[0]
            elif dkwargs.get('key') == True:
                print('Key flag enabled, setting key to True.')
                global key
                key = True
            print('-' * seplen)

            return res
        return wrapped
    return wrap


@decorate
def example(x, y, op='add'):
    if op == 'add':
        return x + y
    elif op == 'sub':
        return x - y


@decorateplus(5, modify=True)
def example2(x, y, op='sub'):
    if op == 'add':
        return x + y
    elif op == 'sub':
        return x - y


@decoratepp(modify=False, key=True)
def example3(x, y, op='mul'):
    if op == 'mul':
        return x * y


if __name__ == '__main__':
    res = example(2, 3)
    print(f'Return value from {example.__name__}:  {res}\n')
    res = example2(5, 2)
    print(f'Return value from {example2.__name__}:  {res}\n')
    if key:
        print('Key true.')
    res = example3(3, 7)
    print(f'Return value from {example3.__name__}:  {res}')
    if key:
        print('Key true.')
