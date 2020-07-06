class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def click_chat_card(self):
        self.driver.find_element_by_xpath("//button[@id='chat']").click()

    def click_map_card(self):
        self.driver.find_element_by_xpath("//a[@id='map']").click()

    def click_landing_button(self):
        self.driver.find_element_by_xpath("//a[@class='landingLink']").click()

