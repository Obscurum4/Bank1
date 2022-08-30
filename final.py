def store(username, password):
    hashed_password = str(hash1(password))
    details = [username, hashed_password]
    f = open("database.txt",'r')
    info = f.read()
    if username in info:     
        print ("Name Unavailable. Please Try Again")
        return main()
    f.close() 
    f = open("database.txt",'w')
    info = info + " " +username + " " + hashed_password
    f.write(info)
    f.close()
    main()


def login(username, password):
    hashed_password1 = str(hash1(password))
    f = open("database.txt",'r')
    info = f.read()
    info = info.split()
    if username in info:
        index = info.index(username) + 1
        usr_password = info[index]
        if hashed_password1 == usr_password:
            print("Success")
            return True
        else:
            print("1st Failure")
            return False
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





def hash1(password):
    list1=[ord(ch) for ch in password]
    final = sum(list1)
    return final



def displayDetails():
  print("Your bank balance is $101")


main()

