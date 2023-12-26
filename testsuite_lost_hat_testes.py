import unittest

from lost_hat_tests import LostHatFrontPageTests
from lost_hat_smoke_tests import LostHatSmokeTests

def smoke_suite_for_lost_hat_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(LostHatFrontPageTests))
    test_suite.addTest(unittest.makeSuite(LostHatSmokeTests))
    return test_suite

runner = unittest.TextTestRunner(verbosity=2)
runner.run(smoke_suite_for_lost_hat_tests())