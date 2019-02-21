""""
Chapter 1: Cracking the code interview
Author: Francisco Velazquez
"""
import datetime

def verify_unique_characters_in_string_solution1(data):
    """
    Question 1.1
    Implement an algorithm to determine if a string has all unique characters.
    What if you can not use additional data structures?

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
    Question 1.1
    Implement an algorithm to determine if a string has all unique characters.
    What if you can not use additional data structures?

    :param data: must be an string
    :return: True if unique characters
    """
    for index in range(len(data)):
        for element in data[index + 1:]:
            if data[index] == element:
                return False
    return True


def verify_unique_characters_in_string_solution3(data):
    """
    Implement an algorithm to determine if a string has all unique characters.
    What if you can not use additional data structures?
    """
    validate_input_values(data)

    new_array = []
    for char in data:
        if char in new_array:
            return False
        else:
            new_array.append(char)
    return True


def validate_input_values(data=None):
    if not isinstance(data, str):
        raise ValueError("data is not string")
    if len(data) == 0:
        raise ValueError("data length is zero")


if __name__ == "__main__":
    input = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    start_sol1 = datetime.datetime.now()
    sol1 = verify_unique_characters_in_string_solution1(input)
    import time
    time.sleep(2)
    start_sol2 = datetime.datetime.now()
    sol2 = verify_unique_characters_in_string_solution2(input)
    start_sol3 = datetime.datetime.now()
    sol3 = verify_unique_characters_in_string_solution3(input)
    end_sol3 = datetime.datetime.now()
    print sol1, sol2, sol3
    sol1_exec_time = start_sol1-start_sol2
    sol2_exec_time = start_sol2-start_sol3
    sol3_exec_time = start_sol3-end_sol3
    print sol1_exec_time.seconds
    print sol2_exec_time.microseconds
    print sol3_exec_time.microseconds
