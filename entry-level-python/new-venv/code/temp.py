#!/usr/bin/env python

fahrenheitTemp=float(input("What temperature (in Fahrenheir) would you like\nconverted to Celsius? "))
celsiusTemp=(fahrenheitTemp-32)*5/9
print(fahrenheitTemp,"F is",round(celsiusTemp,2),"C")
print(str(fahrenheitTemp)+" F is "+ str(round(celsiusTemp,2))+" C")