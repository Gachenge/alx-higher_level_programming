#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            str = "FizzBuzz"
        elif i % 5 == 0:
            str = "Buzz"
        elif i % 3 == 0:
            str = "Fizz"
        else:
            str = i
        print("{} ".format(str), end='')
