""""
Chapter 1: Cracking the code interview
Author: Francisco Velazquez
"""
# region Problem 1.1


def verify_unique_characters_in_string_solution1(data):
    """
    Question 1.1
    Implement an algorithm to determine if a string has all unique characters.
    What if you can not use additional data structures?

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
    Question 1.1
    Implement an algorithm to determine if a string has all unique characters.
    What if you can not use additional data structures?

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
    Implement an algorithm to determine if a string has all unique characters.
    What if you can not use additional data structures?

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
    Implement an algorithm to determine if a string has all unique characters.
    What if you can not use additional data structures?

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


def reverse_string_solution1(data):
    """
    Write code to reverse a C-Style String. (C-String means that 'abcd' is
    represented as five characters, including the null character.)

    :return: reversed string
    """
    validate_input_values(data)
    data_output = ""
    for char in data:
        data_output = char + data_output
    return data_output


def reverse_string_solution2(data):
    """
    Write code to reverse a C-Style String. (C-String means that 'abcd' is
    represented as five characters, including the null character.)

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


def remove_duplicate_char_in_string_solution1(data):
    """
    Design an algorithm and write code to remove the duplicate characters in a string
    without using any additional bu#er. NOTE: One or two additional variables are !ne.
    An extra copy of the array is not.

    :return: string without duplicates
    """
    validate_input_values(data)

    data = list(data)
    for index in range(len(data)):
        for element in data[index + 1:]:
            if data[index] == element:
                data = data[:index] + data[index+1:]
    data = ''.join(data)
    return data


def remove_duplicate_char_in_string_solution1(data):
    """
    Design an algorithm and write code to remove the duplicate characters in a string
    without using any additional bu#er. NOTE: One or two additional variables are !ne.
    An extra copy of the array is not.

    :return: string without duplicates
    """
    validate_input_values(data)

    data = list(data)
    for index in range(len(data)):
        for element in data[index + 1:]:
            if data[index] == element:
                data = data[:index] + data[index+1:]
    data = ''.join(data)
    return data

# endregion Problem 1.3
# region Problem 1.4


def verify_if_two_strings_are_anagrams_solution1(data1, data2):
    """
    Write a method to decide if two strings are anagrams or not.

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
    Write a method to decide if two strings are anagrams or not.

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


def convert_string_to_dict(data):
    skip_char = {}
    for index in range(len(data)):
        char = data[index]
        if char in skip_char:
            skip_char[char] = skip_char[char] + 1
            continue
        skip_char[char] = 1
    return skip_char
# endregion Problem 1.4


def validate_input_values(data=None):
    if not isinstance(data, str):
        raise ValueError("data is not string")
    if len(data) == 0:
        raise ValueError("data length is zero")


if __name__ == "__main__":
    input = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZa"
    # print verify_unique_characters_in_string_solution1(input)
    # print verify_unique_characters_in_string_solution2(input)
    # print verify_unique_characters_in_string_solution3(input)
    # print verify_unique_characters_in_string_solution4(input)
    # print reverse_string_solution1(input)
    # print reverse_string_solution2(input)
    # print remove_duplicate_char_in_string_solution1(input)
    print verify_if_two_strings_are_anagrams_solution2(input, input)
