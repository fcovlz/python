"""
Question 1.1
 Implement an algorithm to determine if a string has all unique characters.
 What if you can not use additional data structures?
"""


def verify_unique_characters_in_string_solution1(data):
    """
    :param data: must be an string
    :return: True if unique characters
    """
    if len(data) > 1:
        for char in data[1:]:
            if data[0] == char:
                return False
        return verify_unique_characters_in_string_solution1(data[1:])
    else:
        return True


def verify_unique_characters_in_string_solution2(data):
    """
    :param data: must be an string
    :return: True if unique characters
    """
    for index in range(len(data)):
        for element in data[index+1:]:
            if data[index] == element:
                return False
    return True
