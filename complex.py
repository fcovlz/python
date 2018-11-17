class Complex(object):
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        print "Object built successfully "

    def abs(self):
        import math
        return math.sqrt((self.r*self.r)+(self.i*self.i))