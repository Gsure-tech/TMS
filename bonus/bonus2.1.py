password = input("Enter password: ")

while password != "pass123":
    password = input("Enter password: ")

if len(password) < 8:
    print("Password is too short")

print("Password is correct!")