#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    int = 0

    for i in range(len(roman_string)):
        if (i != len(roman_string) - 1 and rom[roman_string[i]] <
                rom[roman_string[i + 1]]):
            int += rom[roman_string[i]] * -1
        else:
            int += rom[roman_string[i]]
    return int
