#!/usr/bin/env python

text= input("Enter a message: ")
print("Lowercase "+ text.lower())
print("Uppercase "+text.upper())
print("capitalized "+text.capitalize())
print("Title case "+ text.title())
print("words "+text.split())
sorted_words=sorted(text.split())
print("Alphabetic first word "+sorted_words[0])
print("Alphabetic last word "+sorted_words[-1])