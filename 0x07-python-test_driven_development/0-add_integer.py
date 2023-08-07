#!/usr/bin/python3
def add_integer(first_number, second_number=98):
    if not isinstance(first_number, int) and not
    isinstance(first_number, float):
        raise TypeError("first_number should be an integer")
    if not isinstance(second_number, int) and not
    isinstance(second_number, float):
        raise TypeError("second_number should be an integer")
    if isinstance(first_number, float):
        first_number = int(first_number)
    if isinstance(second_number, float):
        second_number = int(second_number)
    return (first_number + second_number)
