def store(username, password):
    hashed_password = hash1(password)
    print(hashed_password)
    details = [username, hashed_password]
    file = open("database.txt","a")
    file.write(str(username))
    file.write(" ")
    file.write(str(hashed_password))
    file.write("\n")
    file.close()


def login(username, password):
    
    hashed_password1 = str(hash1(password))
    print(hashed_password1)
    for line in open("database.txt","r").readlines(): 
        login_info = line.split()
        print(login_info[0])
        print(login_info[1])
        if username == login_info[0] and hashed_password1 == login_info[1]:
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
