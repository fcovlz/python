# region Object as add data automatically
class AddAttributesAutomatically(object):

    def __init__(self, color, speed, mode):
        """
        Constructor
        """
        self.set_attribute('color', color)
        self.set_attribute('speed', speed)
        self.__setattr__('model', mode)
        self.__setattr__('plat_number', mode)

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
        print("Getting value ...")
        return self._color

    @color.setter
    def color(self, value):
        print("Setting value ...")
        self._color = value

    @property
    def speed(self):
        print("Getting value ...")
        return self._speed

    @speed.setter
    def speed(self, value):
        print("Setting value ...")
        self._speed = value

    @property
    def mode(self):
        print("Getting value ...")
        return self._mode

    @mode.setter
    def mode(self, value):
        print("Setting value ...")
        self._mode = value

# endregion data with decorators
