import unittest
import HtmlTestRunner
from Tests.login import LoginTest
from Tests.landing import LandingTest
from Tests.register import RegisterTest
from Tests.map import MapTest
from Tests.home import HomeTest


def run():
    # test_classes_to_run = [LandingTest, LoginTest, RegisterTest, MapTest, HomeTest]
    test_classes_to_run = [LoginTest]

    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    big_suite = unittest.TestSuite(suites_list)
    runner = HtmlTestRunner.HTMLTestRunner(output="nrt-ftest/report/website/")
    results = runner.run(big_suite)
    exit(0)
