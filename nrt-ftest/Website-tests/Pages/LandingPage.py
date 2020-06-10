class LandingPage:

    def __init__(self, driver):
        self.driver = driver

    def click_app_link(self):
        self.driver.find_element_by_xpath("//input[@value='Application']").click()

    def click_home(self):
        self.driver.find_element_by_xpath("//a[text()='KWILI']").click()

    def click_map(self):
        self.driver.find_element_by_xpath("//a[@href='/map']").click()
