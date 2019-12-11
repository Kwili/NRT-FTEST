class LoginScreen:
    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Se connecter\")").click()
