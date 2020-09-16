import unittest
import HtmlTestRunner
from Website_tests.Tests.landing import LandingTest
from Website_tests.Tests.home import HomeTest
from Website_tests.Tests.map import MapTest
from Website_tests.Tests.chat import ChatTest


def run():
    """
    Function run de Website_tests.

    Lance les classes de tests spécifiées.
    """
    test_classes_to_run = [HomeTest, LandingTest, MapTest, ChatTest]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    big_suite = unittest.TestSuite(suites_list)
    runner = HtmlTestRunner.HTMLTestRunner(output="./report/website/")
    runner.run(big_suite)
    exit(0)
