class SettingsScreen:
    """
    Classe SettingsScreen.

    Recherche les différents élements de l'écran du chat bot à tester.
    """
    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver

    def click_settings_tab(self):
        """Clique sur le bouton settings"""
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'Settings')] | //android.widget.Button[contains(@content-desc,'Réglages')]").click()

    def click_cursor(self, text):
        """Cliquer sur le curseur choisi"""
        self.driver.find_element_by_xpath(f"//android.widget.Switch[@text='{text}']").click()

    def click_language(self, language):
        """Clique sur le bouton langue"""
        self.driver.find_element_by_xpath("//android.widget.Spinner").click()
        self.driver.find_element_by_xpath(f"//android.widget.CheckedTextView[@text='{language}']").click()

    def switch_mode(self):
        """Clique sur le bouton langue"""
        self.driver.find_element_by_xpath("//android.widget.Switch").click()










