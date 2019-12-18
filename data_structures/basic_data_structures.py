from collections import namedtuple
from collections import deque


# region String manipulation
hex_value = 0x1
print("Set specific number of zeros 0x%08X" % hex_value)
print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N',
                                                    longitude='10.5S'))
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
        print(array_of_arrays)

    def string_as_array(self, words):
        """
        Examples
        @:param array_size: size of arrays of arrays
        """
        for word in words:
            print(word)

    def array_properties_test(self, array):
        """
        Examples
        @:param array: array under test
        """
        array.insert(0, -3)
        array.append(5)
        print(array.count(5))
        print(array.insert(0, "-3"))
        print(array.pop())
        print(array.extend('5'))
        print(array.remove('5'))
        print(array.reverse())
        print(array.sort())

        for index, value in enumerate(array):
            print(index)
            print(value)


list1 = [1, 2, 3, 4, 5, 6]
list1 = [num * num for num in list1]
print(list1)

list2 = [255] * 100
print(list2)

list3 = range(0, 10)
print(list3)

list4 = [[0 for index0 in range(10)] for index1 in range(10)]
print(list4)

list5 = [[0] * 10] * 10
print(list5)
# endregion List manipulation


# region tuples
tuple = (1, 2, 3, 4)
a, b, c = "a", "b", "c"

SPEED = namedtuple('cpu_speed', 'MHZ GHZ')(800, 1.3)

modes_tuple = namedtuple('ProductMode', 'modo1 modo2')
MODES = modes_tuple('1', '2')
# endregion tuples


# region hash map
personal_info = {'name': 'Francisco',
                 'age': 2,
                 'occupation': 'Engineer'}

for key, value in personal_info.iteritems():
    print("key {} and value {}".format(key, value))
# endregion has map


# region Queue
queue = []

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(6)
queue.append(7)
queue.append(8)
queue.append(4)

queue.pop()
queue.pop(2)
# endregion Queue


# region Dequeue
queue1 = deque()

queue1.append(1)
queue1.append(2)
queue1.append(3)
queue1.append(6)
queue1.append(7)
queue1.append(8)
queue1.append(4)
queue1.appendleft(0)
queue1.appendleft(-1)
queue1.appendleft(-10)

queue1.popleft()
queue1.pop()
queue1.pop(2)
# endregion Dequeue


# region set
my_set = {1, 2, 3, 4, 5, 6}
my_set.add(10)
my_set.add(7)
my_set.add(8)
my_set.add(-1)
print(my_set)
my_set.pop()
my_set.remove(9)
my_set.remove(3)

for element in my_set:
    print(element)
# endregion set


if __name__ == "__main__":
    # array manipulation
    array_test = ArrayTest()
    array_test.string_as_array(words="hello world")
    array_test.array_properties_test(array=['-2', '-1', '0', 1, 2, 3, 4, 5])
    array_test.create_array_of_arrays(array_size=10)
