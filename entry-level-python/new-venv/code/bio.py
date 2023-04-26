#!/usr/bin/env python

name = input("What´s your name? ")
color = input("What's your favoriate color? ")
age = int(input("How old are you today? "))

print(name)
print("is "+str(age)+" years old")
print("and loves the color "+color+".")

print(name, end=" ")
print("is "+str(age)+" years old", end=" ")
print("and loves the color "+color+".", end=" ")

print(name, "is", age, "years old and loves the color, color", color+".", sep=" ")

fahrenheitTemp=float(input("What temperature (in Fahrenheir) would you like\nconverted to Celsius? "))
celsiusTemp=(fahrenheitTemp-32)*5/9
print(str(fahrenheitTemp)+" F is "+ str(round(celsiusTemp,2))+" C")

