

# region String manipulation
hex_value = 0x1
print "Set specific number of zeros 0x%08X"%hex_value

print '{0}, {1}, {2}'.format('a', 'b', 'c')

print 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N',
                                                    longitude='-115.81W')

# endregion String manipulation


# region List manipulation
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
# endregion List manipulation


# region tuples

tuple = (1, 2, 3, 4)

from collections import namedtuple
SPEED = namedtuple('cpu_speed', 'MHZ GHZ')(800, 1.3)

modes_tuple = namedtuple('ProductMode', 'modo1 modo2')
MODES = modes_tuple('1', '2')

# endregion tuples

if __name__ == "__main__":

    # array manipulation
    array_test = ArrayTest()
    array_test.string_as_array(words="hello world")
    array_test.array_properties_test(array=['-2', '-1', '0', 1, 2, 3, 4, 5])
    array_test.create_array_of_arrays(array_size=10)
    





