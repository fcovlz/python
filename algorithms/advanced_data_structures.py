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

# endregion Linked list

# region Tree

# endregion Tree