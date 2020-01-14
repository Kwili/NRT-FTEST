class RegisterScreen:
    def __init__(self, driver):
        self.driver = driver

    def click_register(self):
        self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"S'inscrire\")").click()

    def click_patient(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Patient')]").click()

    def fill_email(self, email):
        self.driver.find_element_by_xpath("(//android.widget.EditText)[1]").send_keys(email)
        origin_el = self.driver.find_element_by_xpath("(//android.widget.EditText)[5]")
        destination_el = self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'S'INSCRIRE')]")
        self.driver.scroll(origin_el, destination_el)
        destination_el.click()
