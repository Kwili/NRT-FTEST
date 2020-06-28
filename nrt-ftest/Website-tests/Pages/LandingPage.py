class LandingPage:

    def __init__(self, driver):
        self.driver = driver

    def click_navbar_app_link(self):
        self.driver.find_element_by_xpath("//input[@value='Application']").click()

    def click_home(self):
        self.driver.find_element_by_xpath("//a[text()='KWILI']").click()

    def click_map(self):
        self.driver.find_element_by_xpath("//a[@href='/map']").click()

    def click_chat_widget(self):
        self.driver.find_element_by_xpath("//button[@class='rcw-launcher']").click()

    def click_app_apercu_link(self):
        self.driver.find_element_by_xpath("//div[@class='downloadButton']").click()
