
from test_base_class import BaseTest

def TestCase(Test):

    def __init__(self, test_system=None):
        super(TestCase, self).__init__(test_system)

    def test_script(self):
        print "running"


if __name__ == "__main__":
    TEST = Test("system_test")
    RETURN_CODE = TEST.run()
    sys.exit(RETURN_CODE)
