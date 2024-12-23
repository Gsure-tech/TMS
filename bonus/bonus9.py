user_password = input("Enter new password:")

result = []
if len(user_password) >= 8:
    result.append(True)
else:
    result.append(False)

print(result)