class Test(object):
    """
    Base class for all system tests.
    """
    options_dec = None

    def __init__(self, test_system=None):
        """
        Construct a new :obj:`BaseTest` test instance.

        """
        self.test_system = test_system

    def setup(self):
        """
        WIP
        """
        print "SETUP not implemented."

    def start_test(self):
        """
        WIP
        """
        print "start_test method not implemented."

    def verify_results(self):
        """
        WIP
        """
        print "verify_results not implemented."

    def close_test(self):
        """
        WIP
        """
        print self.test_system
        print "close_test method not implemented."

    def run(self):
        """
        WIP
        """
        self.setup()
        self.start_test()
        self.verify_results()
        self.close_test()
        return 1
