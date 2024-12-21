# filenames = ["1.doc","1.report","1.presentation"]
#
# filenames = [filename.replace('.','_')+".txt" for filename in filenames]
# print(filenames)
#
#
# usernames = ["john 1990", "alberta1970", "magnola2000"]
# usernames = [len(username) for username in usernames]
# print(usernames)
#
#
# user_entries = ['10', '19.1', '20']
# user_entries = [float(user_entry) for user_entry in user_entries]
# print(user_entries)
#
# numbers = [10, 20, 30]
# numbers = [num * 2 for num in numbers]
# print(numbers)


user_entries = ['10', '19.1', '20']
user_entries = [float(user_entry) for user_entry in user_entries]

print(sum(user_entries))