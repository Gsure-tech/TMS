def get_average():
    with open("files/data.txt", "r") as file:
        data = file.readlines()
    return data

average = get_average()
print(average)