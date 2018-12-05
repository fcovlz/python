import random
import string


def create_array_integers_min_max(min_number, max_number, length_array):
    array = []
    for index in range(length_array):
        array.append(random.randint(min_number, max_number))
    return array


def create_array_integers(length_array):
    return [random.randint(0, length_array) for _ in range(length_array)]


def create_array_characters(length_array):
    return [random.choice(string.ascii_lowercase) for _ in range(length_array)]


def create_string_characters(length_string):
    _string = ""
    for _ in range(length_string):
        _string += random.choice(string.ascii_lowercase)
    return _string
