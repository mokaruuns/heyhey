def day5_main():
  # if you use ctrl + lbm, so you use multiple cursors
  # print('for example it\'s')
  # print('for example it\'s')
  # print('for example it\'s')
  # ctrl + / fast comment
  # if you write program for yourself, use comments as pseuso-code
  check_password()


def check_password():
  username = input('What\'s your name? ')
  password = input('What\'s your password? ')
  password_lenght = len(password)
  password_stars = '*' * password_lenght
  s = f'{username}, your password {password_stars} is {password_lenght} letters long'
  print(s)