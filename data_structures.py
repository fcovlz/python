
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
