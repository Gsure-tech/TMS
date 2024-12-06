# buttons = ["cancel", "reply", "submit"]
# for i in buttons:
#     print(i.capitalize())

menu = ["pasta", "pizza", "salad"]

user_choice = int(input("Enter the index of the item: "))

message = f"You chose {menu[user_choice]}."
print(message)