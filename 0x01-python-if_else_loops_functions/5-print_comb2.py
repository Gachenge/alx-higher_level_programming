#!/usr/bin/python3
for i in range(100):
    if (i == 99):
        continue
    print(f"{i:02d}, ", end='')
print(f"{i}")
