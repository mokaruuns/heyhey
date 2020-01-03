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
# int and double 
print(type(1))
print(type(1.0))

# operator precedence
print((5 + 4) * 10 / 2) # 45 - wrong, 45.0 is right

print(((5 + 4) * 10) / 2) # 45 - wrong

print((5 + 4) * (10 / 2)) # 45 - wrong

print(5 + (4 * 10) / 2) # 25 - wrong

print(5 + 4 * 10 // 2) # 25 - right

# bin and int
print(bin(5)) # 0b101
print(int('0b101', 2)) # 5

# PI - constant
# _value - global variables
# don't use i, I, o, O in your variables
# use %s isatead +
name = 'Marsel'
age = 18
wrong_using = 'name: ' + name + ', age: ' + str(age) + '.' 
right_using = 'name: %s, age: %s.' % (name, age)
print(wrong_using)
print(right_using)