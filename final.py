def store(username, password):
    hashed_password = hash1(password)
    print(hashed_password)
    details = [username, hashed_password]
    with open(r'D:\Users\Nisar\Documents\GitHub\Bank1\database.txt', 'w') as fp:
        for item in details:
            fp.write("%s\n" % item)


def login(username, password):
    
    hashed_password = hash1(password)
    with open(r'D:\Users\Nisar\Documents\GitHub\Bank1\database.txt', 'w') as fp:
        if database[username] == hashed_password:
            print("Success")
            return True
        else:
            print("Failure")
            return False
    

def signup(username, password):
  
  store(username, password)


def main():

  choice = int(input("Press 1 for login, 2 for signup: "))

  if choice == 1:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    result = login(username, password)
    if result == True: 
      displayDetails()
    else:
      main()

  if choice == 2:
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    signup(username, password)
    main()




def hash1(password):
    list1=[ord(ch) for ch in password]
    final = sum(list1)
    return final



def displayDetails():
  print("Your bank balance is $101")


main()
