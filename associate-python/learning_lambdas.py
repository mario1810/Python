#!/usr/bin/env python

#Function
def sum(a,b):
    return a+b

def square(num):
    return num*num;

print(square(2)) #=>4

#lambda
square_lambda = lambda  num: num * 1

assert square(4) == square_lambda(4)
