
def main():

  choice = int(input("Press 1 for login, 2 for signup"))

  if choice == 1:
    username = get username
    password = get password
    result = login(username, password)
    if result == True: 
      displayDetails()
    else:
      main()

  if choice == 2:
    username = get username
    password = get password
    signup(username, password)
    displayDetails()
  
