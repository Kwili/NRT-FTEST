import unittest
import HtmlTestRunner
from Tests.loginMobile import LoginMobileTest
from Tests.mapMobile import MapMobileTest


def run():
    test_classes_to_run = [LoginMobileTest, MapMobileTest]

    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    big_suite = unittest.TestSuite(suites_list)
    runner = HtmlTestRunner.HTMLTestRunner(output="./report/website/")
    runner.run(big_suite)
