# region Object as add data automatically
class AddAttributesAutomatically(object):

    def __init__(self, color, speed, mode):
        """
        Constructor
        """
        self.set_attribute('color', color)
        self.set_attribute('speed', speed)
        self.set_attribute('model', mode)

    def set_attribute(self, attr_name, attr_value):
        """
        Set attribute on class
        """
        setattr(self, attr_name, attr_value)

# endregion Object as data structure


# region data with decorators
class AddAttributes(object):
    def __init__(self):
        self._color = None
        self._speed = None
        self._mode = None

    @property
    def color(self):
        print "Getting value ..."
        return self._color

    @color.setter
    def color(self, value):
        print "Setting value ..."
        self._color = value

    @property
    def speed(self):
        print "Getting value ..."
        return self._speed

    @speed.setter
    def speed (self, value):
        print "Setting value ..."
        self._speed = value

    @property
    def mode(self):
        print "Getting value ..."
        return self._mode

    @mode.setter
    def mode (self, value):
        print "Setting value ..."
        self._mode = value

# endregion data with decorators


# region Linked List
class NodeLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.day = None

    def traverse(self):
        node = self.day
        while node is not None:
            print node.value
            node = node.next

    def insert_right(self, value):
        new_node = NodeLinkedList(value)
        if self.day is None:
            self.day = new_node
        else:
            node = self.day
            while node.next is not None:
                node = node.next
            node.next = new_node


def linked_list_sample():
    # create nodes
    days_of_the_week = LinkedList()
    days_of_the_week.insert_right('monday')
    days_of_the_week.insert_right('tuesday')
    days_of_the_week.insert_right('wednesday')
    days_of_the_week.insert_right('thursday')
    days_of_the_week.insert_right('friday')
    days_of_the_week.insert_right('saturday')
    days_of_the_week.insert_right('sunday')

    days_of_the_week.traverse()

# endregion Linked list


# region Tree
class NodeBinaryTree(object):

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = NodeBinaryTree(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = NodeBinaryTree(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = NodeBinaryTree(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print "Value already in tree"

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print  cur_node.value
            self._print_tree(cur_node.right)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left, cur_height + 1)
        right_height = self._height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
                return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left is not None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._search(value, cur_node.right)
        else:
            return False


from random import randint
def fill_tree(tree, num_elem, max_int):
    for index in range(num_elem):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree


def tree_sample():
    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(10)
    tree = fill_tree(tree, 100, 1000)
    tree.print_tree()
    print "tree height is ", str(tree.height())

    print tree.search(2)
    print tree.search(0)
    print tree.search(1010)

# endregion Tree
