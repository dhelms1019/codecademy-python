# takes first three letters of first name and first four letters of last name
def username_generator(first_name, last_name):
  username = ""

  if len(first_name) < 3:
    username = first_name
  else:
    username = first_name[:3]
  
  if len(last_name) < 4:
    username += last_name
  else:
    username += last_name[:4]
  
  return username

# takes username and shifts all letters one to the right
def password_generator(user_name):
  password = ""
  idx = -1

  for letter in user_name:
    password += user_name[idx]
    idx += 1

  return password
#   password = user_name[len(user_name) - 1] + user_name[:len(user_name) - 1]
#   return password

print(username_generator("john", "doe"))
print(password_generator("johdoe"))