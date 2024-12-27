# def get_maximum():
#     celsius_local = [14, 15.1, 12.3]
#     maximum = max(celsius_local)
#     return maximum
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)
"""
def speed(distance, time):
    return distance / time


print(speed(200, 4))

"""


def calculate_time( h,g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)


