#!/bin/python
import os
import string
LOWER_CASE = string.ascii_lowercase
UPPER_CASE = string.ascii_uppercase


# Complete the caesarCipher function below.
def caesar_cipher(s, k):
    new_string = ""
    for character in s:
        if not is_character(character):
            new_string += character
        else:
            new_string += get_character(character, k)
    return new_string


def is_character(character):
    if is_upppercase(character) or is_lowercase(character):
        return True
    else:
        return False


def is_lowercase(character):
    ch_ascii_index = ord(character)
    if 122 >= ch_ascii_index >= 97:
        return True
    else:
        return False


def is_upppercase(character):
    ch_ascii_index = ord(character)
    if 90 >= ch_ascii_index >= 65:
        return True
    else:
        return False


def get_character(character, offset):
    new_char = None
    offset = offset % len(string.ascii_lowercase)
    if is_lowercase(character) and (offset + ord(character) <= 122):
            new_char = chr(ord(character) + offset)
    elif is_upppercase(character) and (offset + ord(character) <= 90):
            new_char = chr(ord(character) + offset)
    else:
            new_char = chr(ord(character) + offset - len(string.ascii_lowercase))
    return new_char
    
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    k = int(input())
    result = caesar_cipher(s, k)
    fptr.write(result + '\n')
    fptr.close()
