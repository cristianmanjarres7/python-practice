# Simple Login System

username = input("Username: ")
password = input("Password: ")

if username == "cristian" and password == "Dios7":
    print("Access granted")
elif username != "cristian":
    print("Incorrect username")
else:
    print("Incorrect password")