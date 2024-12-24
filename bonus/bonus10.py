try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectangle length: "))

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number. ")