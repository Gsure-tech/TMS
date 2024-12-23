user_password = input("Enter new password:")

result = {}
if len(user_password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in user_password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in user_password:
    if i.isupper():
        uppercase = True

result["upper_case"] = uppercase
print(result)
if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")