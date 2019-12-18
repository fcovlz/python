from frameworks.test_runner.test_framework import TestFramework


class TestBase(TestFramework):
    """
    Base class for all system tests.
    """
    options_dec = None

    def __init__(self, result=None, platform=None):
        """
        Construct a new :obj:`BaseTest` test instance.

        """
        self.result = result
        self.test_system = platform

    def test_script(self):
        self.result = 1
        print("all pass")


