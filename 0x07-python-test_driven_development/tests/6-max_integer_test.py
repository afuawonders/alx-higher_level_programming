#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to  return the max integer in a list of integers
        Return  None if list is empty
    """
    if len(list) == 0:
        return (None)
    answer = list[0]
    index = 1
    while index < len(list):
        if list[index] > answer:
            answer = list[index]
        index += 1
    return (answer)
