import unittest

from lost_hat_login_page_tests import LostHatLoginPageTests
from lost_hat_front_page_tests import LostHatFrontPageTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(LostHatLoginPageTests('test_log_page_website_title'))
    test_suite.addTest(LostHatLoginPageTests('test_login_text_header'))
    test_suite.addTest(LostHatFrontPageTests('test_all_products_have_price_in_pln_on_main_page'))
    test_suite.addTest(unittest.makeSuite(LostHatFrontPageTests))
    return test_suite

runner = unittest.TextTestRunner(verbosity = 2)
runner.run(sanity_suite())
