
import random

result = 0
while True:
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound"))

    result = random.randrange(lower_bound, upper_bound)
    print(result)