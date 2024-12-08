filenames = ["1.doc","1.report","1.presentation"]

filenames = [filename.replace('.','_')+".txt" for filename in filenames]
print(filenames)


usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(username) for username in usernames]
print(usernames)