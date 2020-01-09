def day6_main():
  basket = ['a', 'b', 'c']
  basket.append('d')
  basket.extend([1, 2, 3])
  basket.remove('a')
  basket.pop()
  print(basket)