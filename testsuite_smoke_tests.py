import unittest

from lost_hat_smoke_tests import LostHatSmokeTests
from lost_hat_smoke_tests_2 import LostHatSmokeTests2

def smoke_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(LostHatSmokeTests))
    test_suite.addTest(unittest.makeSuite(LostHatSmokeTests2))
    return test_suite

runner = unittest.TextTestRunner(verbosity = 2)
runner.run(smoke_suite())
