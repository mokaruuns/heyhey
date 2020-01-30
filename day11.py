def day11_main():
  print(range(10))
  print(list(range(10)))
  print(list(range(1,10, 2)))
  print(list(range(10,0,-1)))
  use_enumerate()

def use_enumerate():
  a = [1,2,3,4]
  s = 'abcdefg'
  for i, char in enumerate(s):
    print(i, char)
  print('---')
  for i, number in enumerate(a):
    print(f'{i} element is {number}')