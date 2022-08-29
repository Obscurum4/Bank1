def signup(username, password):

  checkPasswordStuff()
  
  storeData(username, password)


def isPasswordTooShort(password):
  if len(password) < 7:
    return True
  else:
    return False
