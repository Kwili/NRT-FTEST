import unittest
import HtmlTestRunner
from Mobile_tests.Tests.mapMobile import MapMobileTest
from Mobile_tests.Tests.botMobile import BotMobileTest
from Mobile_tests.Tests.settingsMobile import SettingsMobileTest
from Mobile_tests.Tests.contactMobile import ContactMobileTest


def run():
    """
    Function run de Mobile_tests.

    Lance les classes de tests spécifiées.
    """
    test_classes_to_run = [BotMobileTest, SettingsMobileTest, ContactMobileTest]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    big_suite = unittest.TestSuite(suites_list)
    runner = HtmlTestRunner.HTMLTestRunner(output="./report/website/")
    runner.run(big_suite)
