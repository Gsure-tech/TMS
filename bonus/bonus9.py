user_password = input("Enter new password:")

result = []
if len(user_password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False
for i in user_password:
    if i.isdigit():
        digit = True
result.append(digit)

print(result)