class LoginScreen:
    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Se connecter\")").click()

    def fill_id(self):
        self.driver.find_element_by_xpath("(//android.widget.EditText)[1]").send_keys("jean-baptiste.melet@epitech.eu")
        self.driver.find_element_by_xpath("(//android.widget.EditText)[2]").send_keys("azertyuiop")
