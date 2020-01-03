print('Hello, Wolrd!')

#day two
def get_multiplier(a):
    def out(b):
        return (a+1) * b
    return out
multiply_by_3 = get_multiplier(4)(10)
print(multiply_by_3)

def count(start, step):
    while True:
        yield start
        start += step
counter = count(10, 2)
print(next(counter), next(counter), next(counter))

from functools import wraps

def debug(func):
    @wraps(func)
    def out(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return out

@debug
def add(x, y):
    return x + y