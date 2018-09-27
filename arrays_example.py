"""
@ Description
    Brief example of how arrays work

@ Pass/Fail @b criteria
    None

@ Usage
    From terminal:
        arrays_example.py
"""


class ArrayTest:

    def __init__(self):
        pass

    def create_array_of_arrays(self, array_size):
        """
        Examples
        @:param array_size: size of arrays of arrays
        """
        array_of_arrays = [[] for _ in range(array_size)]
        print array_of_arrays

    def string_as_array(self, words):
        """
        Examples
        @:param array_size: size of arrays of arrays
        """
        for word in words:
            print word

    def array_properties_test(self, array):
        """
        Examples
        @:param array: array under test
        """
        array.insert(0, -3)
        array.append(5)

        print array.count(5)
        print array.insert(0, "-3")
        print array.pop()
        print array.extend('5')
        print array.remove('5')
        print array.reverse()
        print array.sort()

        for index, value in enumerate(array):
            print index
            print value


if __name__ == "__main__":
    array_test = ArrayTest()
    array_test.string_as_array(words="hello world")
    array_test.array_properties_test(array=['-2', '-1', '0', 1, 2, 3, 4, 5])
    array_test.create_array_of_arrays(array_size=10)




