import database.txt

def login(username, password):

  hashed_password = hash(password)

  if database[username] == hashed_password:
    print("Success")
    return True
  else:
    print("Failure")
    return False
