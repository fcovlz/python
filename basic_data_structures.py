
car = "Camaro SS"

def super_car():
    print car
    
def super_car1():
    car = "Challenger SRT8"
    print car
    
def super_car2():
    global car
    car = "Viper SRT10"
    print car

class RequestData(object):
"""
Class for Device Registers
"""
def __init__(self, color="", velocidad="", modelo=""):
    """
    Constructor
    """
    self.set_attribute('color', color)
    self.set_attribute('velocidad', velocidad)
    self.set_attribute('modelo', modelo)

def set_attribute(self, attr_name, attr_value):
    """
    Set attribute on class
    """
    setattr(self, attr_name, attr_value)
    
    
"Operation failed at 0x%08X - %s" % (address, value)

'{>>> '{0}, {1}, {2}'.format('a', 'b', 'c')
'a, b, c'

>>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'



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
    
from collections import namedtuple
modes_tuple = namedtuple('ProductMode', 'modo1 modo2')
MODES = modes_tuple('1', '2')


tupl = (1, 2, 3, 4)

