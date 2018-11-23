class Test(object):
    """
    Base class for all system tests.
    """
    options_dec = None

    def __init__(self, result=None, test_system=None):
        """
        Construct a new :obj:`BaseTest` test instance.

        """
        self.result = result
        self.test_system = test_system

    def setup(self):
        """
        WIP
        """
        print "SETUP not implemented."

    def initiate(self):
        """
        WIP
        """
        print "INITIATE method not implemented."

    def complete(self):
        """
        WIP
        """
        print "COMPLETE not implemented."

    def teardown(self):
        """
        WIP
        """
        print self.result
        print self.test_system
        print "TEARDOWN method not implemented."

    def run(self):
        """
        WIP
        """
        self.setup()
        self.initiate()
        self.complete()
        self.teardown()
        return 1
