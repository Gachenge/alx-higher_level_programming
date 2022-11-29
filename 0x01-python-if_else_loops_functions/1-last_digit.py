#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number % 10
if number < 0:
    num *= -1
str = "Last digit of {} is {}".format(number, num) 
if num > 5:
    print(str, "and is greater than 5")
elif num == 0:
    print(str, "and is 0")
else:
    print(str, "and is less than 6 and not 0")
