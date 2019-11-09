from selenium import webdriver
import unittest
import HtmlTestRunner

from Tests.login import *
from Tests.landing import *
from Tests.register import *
from Tests.map import *
from Tests.home import *

if __name__ == '__main__':
    test_classes_to_run = [LandingTest, LoginTest, RegisterTest, MapTest, HomeTest]

    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    big_suite = unittest.TestSuite(suites_list)
    runner = HtmlTestRunner.HTMLTestRunner(output="./report")
    results = runner.run(big_suite)
    exit(0)
