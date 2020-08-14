class MapScreen:
    def __init__(self, driver):
        self.driver = driver

    def click_allow_geo(self):
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button").click()

    def click_rechercher(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Rechercher']").click()

    def click_transport(self):
        self.driver.find_element_by_class_name("android.widget.Spinner").click()

    def choose_transport(self, index):
        self.driver.find_element_by_xpath(f"(//android.widget.CheckedTextView)[{index}]").click()

    def has_found_itinary(self):
        return self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Distance')]").click()

    def click_votre_position(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Votre')]").click()

    def write_position(self, location):
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'Votre')]").send_keys(location)
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'3 Avenue Montaigne, Paris')]").click()

    def click_plus(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='+']").click()

    def click_najma(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Najma']").click()

    def click_return(self):
        self.driver.find_element_by_xpath("//android.widget.ImageView").click()






