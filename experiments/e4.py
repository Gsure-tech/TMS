user_input = input("Enter a new member")

file = open(f"../files/members.txt", 'r')
existing_files = file.readlines()
file.close()
existing_files.append(user_input)

file = open(f"../files/members.txt", 'w')
file.writelines(existing_files)
file.close()