def day8_main():
  # we use unpacking lists
  a, b, *other, q, z = [1,2,3,4,5,6,7,8]
  print(a)
  print(b)
  print(other)
  print(q)
  print(z)

  # dictionary
  user = {
    'age' : 12,
    'is_male' : False
  }
  x = ('key1', 'key2', 'key3')
  y = (1,2,3)
  thisdict = dict.fromkeys(x, y)
  thisdict.pop('key2')
  thisdict.popitem()
  thisdict.setdefault('key2', 123)
  thisdict.update({'key1':'1'})
  print(thisdict)