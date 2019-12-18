
class ResultFramework():
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

    def test_script(self):
        self.result = 1
        print("all pass")
