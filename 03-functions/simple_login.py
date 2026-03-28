# simple_login.py

def login_system(username, password):
    if username != "cristian":
        return "Incorrect username"
    elif password != "Dios7":
        return "Incorrect password"
    else:
        return "Access granted"


username = input("Username: ")
password = input("Password: ")

print(login_system(username, password))