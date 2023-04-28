#!/usr/bin/env  python

valueUser=int(input("How many values shoudl we process:"))
for value in range(1,valueUser+1):
    if value % 5==0 and value % 3==0:
        print("FizzBuzz")
    elif value%5==0:
        print("Fizz")
    elif value%3==0:
        print("Buzz")
    else:
        print(value)