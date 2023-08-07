#!/usr/bin/python3
def say_my_name(firstName, lastName=""):
    if not isinstance(firstName, str):
        raise TypeError("first name must be a string")
    if not isinstance(lastName, str):
        raise TypeError("last name must be a string")
    print("My name is {:s} {:s}".format(firstName, lastName))
