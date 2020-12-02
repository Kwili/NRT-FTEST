class ContactScreen:
    """
    Classe SettingsScreen.

    Recherche les différents élements de l'écran du chat bot à tester.
    """
    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver

    def click_contact_tab(self):
        """Clique sur le bouton settings"""
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'Contact')]").click()

    def write_name(self, text):
        """Clique sur le bouton langue"""
        self.driver.find_element_by_xpath(f"//android.widget.EditText[1]").send_keys(text)

    def write_phone(self, text):
        """Clique sur le bouton langue"""
        self.driver.find_element_by_xpath(f"//android.widget.EditText[2]").send_keys(text)

    def write_message(self, text):
        """Clique sur le bouton langue"""
        self.driver.find_element_by_xpath(f"//android.widget.EditText[3]").send_keys(text)

    def click_confirm(self):
        """Clique sur le bouton langue"""
        self.driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()




