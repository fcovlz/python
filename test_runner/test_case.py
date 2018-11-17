
from test_base_class import BaseTest

def TestCase(Test):

    def __init__(self, result=None, test_system=None):
        super(TestCase, self).__init__(result, test_system)

    def complete(self):
        print "running"


if __name__ == "__main__":
    TEST = Test("resultado", "system_test")
    RETURN_CODE = TEST.run()
    sys.exit(RETURN_CODE)
