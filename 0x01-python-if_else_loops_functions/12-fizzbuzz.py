#!/usr/bin/python3
def fizzbuzz():
    str1 = "FizzBuzz"
    str2 = "Buzz"
    str3 = "Fizz"
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            str = str1
        elif i % 5 == 0:
            str = str2
        elif i % 3 == 0:
            str = str3
        else:
            str = i
        print("{} ".format(str), end='')
