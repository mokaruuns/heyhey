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

# day 3
long_string = '''
hello
it's long string
'''
print(long_string)

# escape sequences 
print('It\'s very easy, but \"hard\" and \nand not easy. \t It\'s just example')

# formatted strings
name = 'Marsel'
age = '18'
wrong_info = 'My name is ' + name + '. I\'m ' + str(age) + ' years old.'
info = f'My name is {name}. I\'m {age} years old.'
print(wrong_info)
print(info) # it's most useful, but 
python2_format = 'My name is {}. I\'m {} years old.'.format(name, age)
python2_format2 = 'My name is {age}. I\'m {name} years old.'.format(name = 'Mars', age = '11')
print(python2_format) 
print(python2_format2)

from string import Template # шаблонные строки
t = Template('Hey, $name!') 
print(t.substitute(name=name))
#Если ваши строки форматирования поддерживаются пользователями, используйте шаблонные строки (способ 4), чтобы избежать проблем с уязвимостью программы. В противном случае, воспользуйтесь литеральной интерполяцией строк / f-строками (способ 3), если вы используете Python 3.6+ и “новым способом” с str.format (способ 2), если не пользуетесь Python 3.6.


# Вот ваш супер-секретный ключ:
SECRET = 'this-is-a-secret'
 
class Error:
    def __init__(self):
        pass
 
# Злоумышленник может создать форматную строку, которая
# может считать данные из общего словаря:
user_input = '{error.__init__.__globals__[SECRET]}'
 
# Это позволяет ему профильтровать конфиденциальную информацию
# такую, как секретный ключ:
err = Error()
 
print(user_input.format(error=err))
print(Template(user_input).substitute(error=err))
# Вывод: 'this-is-a-secret'


