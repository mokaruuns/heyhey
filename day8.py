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

  dictionary()

def dictionary():
  #1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

  #2 iterate and print all the keys in the above user.

  #3 Add a new weapon to your user

  #4 Add a new key to include 'is_banned'. Set it to false

  #5 Ban the user by setting the previous key to True

  #6 create a new user2 my copying the previous user and update the age value and username value. 

  user_profile = dict.fromkeys(('age', 'username', 'weapons', 'is_active', 'clan'))
  print(*user_profile.keys())
  user_profile.update({'weapons': 'gun'})
  user_profile.update({'is_banned': False})
  user_profile['is_banned'] = True 
  user2_profile = user_profile.copy()    
  user2_profile.update({'age': 11})
  user2_profile.update({'username': 'kjsohs'})
  print(user_profile)
  print(user2_profile)