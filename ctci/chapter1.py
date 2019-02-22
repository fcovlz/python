""""
Chapter 1: Cracking the code interview
Author: Francisco Velazquez
"""
# region Problem 1.1
"""
Implement an algorithm to determine if a string has all unique characters.
What if you can not use additional data structures?
"""


def verify_unique_characters_in_string_solution1(data):
    """
    :param data: must be an string
    :return: True if unique characters in string
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
    :return: True if unique characters in string
    """
    for index in range(len(data)):
        for element in data[index + 1:]:
            if data[index] == element:
                return False
    return True


def verify_unique_characters_in_string_solution3(data):
    """
    :param data: must be an string
    :return: True if unique characters in string
    """
    validate_input_values(data)
    new_array = []
    for char in data:
        if char in new_array:
            return False
        else:
            new_array.append(char)
    return True


def verify_unique_characters_in_string_solution4(data):
    """
    :param data: must be an string
    :return: True if unique characters in string
    """
    validate_input_values(data)
    data = sorted(data)
    new_array = []
    for char in data:
        if char in new_array:
            return False
        else:
            new_array.append(char)
    return True


# endregion Problem 1.1
# region Problem 1.2
""""
Write code to reverse a C-Style String. (C-String means that 'abcd' is
represented as five characters, including the null character.)
"""


def reverse_string_solution1(data):
    """
    :return: reversed string
    """
    validate_input_values(data)
    data_output = ""
    for char in data:
        data_output = char + data_output
    return data_output


def reverse_string_solution2(data):
    """
    :return: reversed string
    """
    validate_input_values(data)
    data = list(data)
    for index in range(len(data)/2):
        first_char = data[index]
        data[index] = data[-1 - index]
        data[-1 - index] = first_char
    data = ''.join(data)
    return data


# endregion Problem 1.2
# region Problem 1.3
""""
Design an algorithm and write code to remove the duplicate characters in a string
without using any additional bu#er. NOTE: One or two additional variables are !ne.
An extra copy of the array is not.
"""


def remove_duplicate_char_in_string_solution1(data):
    """
    :return: string without duplicates
    """
    validate_input_values(data)

    data = list(data)
    for index in range(len(data)):
        for element in data[index + 1:]:
            if data[index] == element:
                data = data[:index] + data[index + 1:]
    data = ''.join(data)
    return data


# endregion Problem 1.3
# region Problem 1.4
"""
Write a method to decide if two strings are anagrams or not.
"""


def verify_if_two_strings_are_anagrams_solution1(data1, data2):
    """
    :param data1: String reference 1
    :param data2: String reference 2
    :return:
    """
    if sorted(data1) == sorted(data2):
        return True
    else:
        return False


def verify_if_two_strings_are_anagrams_solution2(data1, data2):
    """
    :param data1: String reference 1
    :param data2: String reference 2
    :return:
    """
    if len(data1) != len(data2):
        return False
    dict_data1 = convert_string_to_dict(data1)
    dict_dat2 = convert_string_to_dict(data2)
    if dict_data1 == dict_dat2:
        return True
    else:
        return False


# endregion Problem 1.4
# region Problem 1.5
"""
Write a method to replace all spaces in a string with '%20'
"""


def replace_spaces_in_string_solution1(data):
    data_out = ""
    for char in data:
        if char == ' ':
            data_out = data_out + '%20'
        else:
            data_out = data_out + char
    return data_out


# endregion Problem 1.5
# region Problem 1.6
"""
Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. 
"""


def rotate_image_by_90_degrees_solution1(matrix):
    x_axis = len(matrix[0])
    matrix_output = [[] for _ in xrange(x_axis)]
    for row in matrix:
        for index in range(len(row)):
            matrix_output[-1 - index].append(row[index])
    return matrix_output


# endregion Problem 1.6
# region Problem 1.7
"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row 
and column is set to 0
"""


def search_zero_element_set_0_row(matrix):
    for index in range(len(matrix)):
        row = matrix[index]
        for element in row:
            if element == 0:
                matrix[index] = [0] * len(row)
                break
    return matrix


# endregion Problem 1.7
# region Problem 1.8
"""
Assume you have a method isSubstring which checks if one word is a substring of
another. Given two strings, s1 and s2, write code to check if s2 is a rotation 
of s1 using only one call to isSubstring (i.e., 'waterbottle' is a rotation of 
'erbottlewat').
"""


def isSubstring(data1, data2):
    if data1 == data2:
        return True
    for index in range(len(data2)):
        first_char = data2[0]
        data2 = data2[1:] + first_char
        if data1 == data2:
            return True
    return False

# endregion Problem 1.8
# region Utilities


def convert_string_to_dict(data):
    skip_char = {}
    for index in range(len(data)):
        char = data[index]
        if char in skip_char:
            skip_char[char] = skip_char[char] + 1
            continue
        skip_char[char] = 1
    return skip_char


def validate_input_values(data=None):
    if not isinstance(data, str):
        raise ValueError("data is not string")
    if len(data) == 0:
        raise ValueError("data length is zero")
# endregion Utilities


if __name__ == "__main__":
    input = "abcd efghijklmnopq rstuvwxy z1234567890ABCDEFGHIJKLM NOPQRSTUVWXYZ"
    # print verify_unique_characters_in_string_solution1(input)
    # print verify_unique_characters_in_string_solution2(input)
    # print verify_unique_characters_in_string_solution3(input)
    # print verify_unique_characters_in_string_solution4(input)
    # print reverse_string_solution1(input)
    # print reverse_string_solution2(input)
    # print remove_duplicate_char_in_string_solution1(input)
    # print verify_if_two_strings_are_anagrams_solution2(input, input)
    # print replace_spaces_in_string_solution1(input)
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[1, 2, 3], [4, 5, 6]]
    # matrix = rotate_image_by_90_degrees_solution1(matrix)
    # print "hello world"
    # print matrix
    # print rotate_image_by_90_degrees_solution1(matrix)
    # print search_zero_element_set_0_row(matrix)
    substring1 = "waterbottle"
    substring2 = "erbottlewat"
    print isSubstring(substring1, substring2)