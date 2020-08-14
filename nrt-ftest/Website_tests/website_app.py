import unittest
import HtmlTestRunner
from Website_tests.Tests.landing import LandingTest
from Website_tests.Tests.home import HomeTest
from Website_tests.Tests.map import MapTest


def run():
    test_classes_to_run = [HomeTest, LandingTest, MapTest]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    big_suite = unittest.TestSuite(suites_list)
    runner = HtmlTestRunner.HTMLTestRunner(output="./report/website/")
    runner.run(big_suite)
    exit(0)