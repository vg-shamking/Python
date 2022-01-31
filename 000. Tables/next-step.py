#!/bin/python3
import sys
from datetime import datetime as dt

def nl():
	print('\n')

print("Importing Modules.")
nl()

print(sys.version)
print(dt.now())

nl()
letter ="A"
word = "Apple"
print(letter.lower() in word.lower())

#Dictionaries - key/value pairs {}
nl()
employees = {"white Russian": 7, "HR": ["bob", "linda", "tina"], "IT": "Rob"}

print(employees)
nl()
employees.update({"IT": ["Helen", "Neal"]})
print(employees)
nl()
employees["HR"] += ["olga", "phil"]
print(employees)



