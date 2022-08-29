def hash():
  password = input("Enter your password: ")
  list=[ord(ch) for ch in password]
  print(list)
  hashed_password = (sum(list))
  print(hashed_password)

#hash(password)
hash()
  
