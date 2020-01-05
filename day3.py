class Error:
      def __init__(self):
          pass
from string import Template # шаблонные строки
# Вот ваш супер-секретный ключ:
SECRET = 'this-is-a-secret'

def day3_main():
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

  t = Template('Hey, $name!') 
  print(t.substitute(name=name))
  #Если ваши строки форматирования поддерживаются пользователями, используйте шаблонные строки (способ 4), чтобы избежать проблем с уязвимостью программы. В противном случае, воспользуйтесь литеральной интерполяцией строк / f-строками (способ 3), если вы используете Python 3.6+ и “новым способом” с str.format (способ 2), если не пользуетесь Python 3.6.

  # Злоумышленник может создать форматную строку, которая
  # может считать данные из общего словаря:
  user_input = '{error.__init__.__globals__[SECRET]}'
  # Это позволяет ему профильтровать конфиденциальную информацию
  # такую, как секретный ключ:
  err = Error()
  print(user_input.format(error=err))
  print(Template(user_input).substitute(error=err))
  # Вывод: 'this-is-a-secret'
  