from frameworks.test_runner.test_base import TestBase
from frameworks.test_runner.result_framework import ResultFramework
from frameworks.test_runner.platform_framework import PlatformFramework
import sys


class TestCase(TestBase):

    def __init__(self, result=None, platform=None):
        super.__init__(result, platform)

    def test_script(self):
        print("running")


if __name__ == "__main__":
    TEST = TestCase(ResultFramework, PlatformFramework)
    RETURN_CODE = TEST.run()
    sys.exit(RETURN_CODE)
