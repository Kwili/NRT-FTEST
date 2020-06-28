import unittest
import HtmlTestRunner
from Tests.login import LoginTest
from Tests.landing import LandingTest
from Tests.register import RegisterTest
from Tests.map import MapTest


def run():
    # test_classes_to_run = [LandingTest, LoginTest, RegisterTest, MapTest]
    test_classes_to_run = [LandingTest]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    big_suite = unittest.TestSuite(suites_list)
    runner = HtmlTestRunner.HTMLTestRunner(output="./report/website/")
    runner.run(big_suite)
    exit(0)
