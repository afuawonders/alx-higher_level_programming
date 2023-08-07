#!/usr/bin/python3
def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size should be an integer")
    if size < 0:
        raise ValueError("size should be >= 0")
    for index in range(size):
        print("x" * size)
