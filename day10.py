def day10_main():
  # compare is and ==
  print(1 == True)
  print(1 is True)
  print(1.0 == 1)
  print(1.0 is 1)

  # iterable 
  user = {
    'mars': 'jss',
    'kops': 'okss',
    'roas': 'sqiz'
  }
  for key, value in user.items():
    print(key, value)