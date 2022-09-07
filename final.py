import random
import string

def store(username, password, pepper):
    salt = get_salt()
    final_hash = salt + pepper + password
    hashed_password = str(hash1(final_hash))
    f = open("database.txt",'r')
    info = f.read()
    if username in info:     
        print ("Name Unavailable. Please Try Again")
        return main()
    f.close()
    f = open("database.txt",'w')
    info = info + " " +username + " "  + hashed_password + " " + salt
    f.write(info)
    f.close()
    main()


def login(username, password, pepper):
       
    f = open("database.txt",'r')
    info = f.read()
    info = info.split()
    if username in info:
        index = info.index(username) + 1
        index1 = info.index(username) + 2
        stored_salt = info[index1]
        combination_hash = info[index1] + pepper + password
        hashed_password1 = str(hash1(combination_hash))
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
    

def signup(username, password,pepper):
  
  store(username, password, pepper)
  print("Sign-up successful!")


def main():
  pepper = "n3r@u_iTyrzN35K"
  choice = int(input("Press 1 for login, 2 for signup: "))

  if choice == 1:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    result = login(username, password, pepper)
    if result == True: 
      displayDetails()
    else:
        main()
    


  if choice == 2:
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    signup(username, password, pepper)





def hash1(password):
    list1=[ord(ch) for ch in password]
    final = sum(list1)
    return final


def get_salt():
    salt = ""
    for i in range(10):
        character = (''.join(random.choice(string.digits + string.ascii_letters)))
        salt = salt + character
    return salt
    

def displayDetails():
  print("Your bank balance is $101")





main()
