class BotScreen:
    def __init__(self, driver):
        self.driver = driver

    def click_bot_tab(self):
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'Bot')]").click()

    def send_text(self, text):
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(text)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Send']").click()






