"""
@ Description
    Complex numbers handling in Python

@ Pass/Fail @b criteria
    N/A

@ Usage
    From terminal:
        complex_num.py
"""
import math


class Complex:
    def __init__(self):
        print "Object built successfully "

    def absolute(self, realpart, imagpart):
        return math.sqrt((realpart * realpart) + (imagpart * imagpart))


if __name__ == "__main__":
    complex_numbers = Complex()
    real_number = 5
    imaginary_number = -2j
    absolute_value = complex_numbers.absolute(real_number, imaginary_number)
