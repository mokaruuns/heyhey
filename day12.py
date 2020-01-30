def first_def(a,b):
  def second_def(a,b):
    return a+b
  return second_def
def day12_main():
  print("hello, day12")
  k = first_def(1,2)
  print(k(1,3))