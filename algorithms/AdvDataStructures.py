# region Object as data structure
class RequestData(object):
    """
    Class for Device Registers
    """

    def __init__(self, color, speed, model):
        """
        Constructor
        """
        self.set_attribute('color', color)
        self.set_attribute('speed', speed)
        self.set_attribute('model', model)
        # or
        self.color = color
        self.speed = speed
        self.model = model

    def set_attribute(self, attr_name, attr_value):
        """
        Set attribute on class
        """
        setattr(self, attr_name, attr_value)
# endregion Object as data structure

# region Linked List

class LinkedList(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value:
            if not self.right:
                self.right = LinkedList(value)
        else:
            if not self.left:
                self.left = LinkedList(value)


def linked_list_test(self):
    linkedlist = LinkedList


# endregion Linked list

# region Tree

# endregion Tree