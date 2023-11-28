#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
if number < 0:
    lastdigit = -(lastdigit)
str = "Lastdigit of {} is {}".format(number, lastdigit)
if lastdigit > 5:
    print(f"{str} and is greater than 5")
elif lastdigit == 0:
    print(f"{str} and is 0")
elif lastdigit < 6:
    print(f"{str} and is less than 6")
