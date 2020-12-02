class BotScreen:
    """
    Classe BotScreen.

    Recherche les différents élements de l'écran du chat bot à tester.
    """
    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver

    def click_bot_tab(self):
        """Clique sur le bouton du chat bot"""
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'Bot')]").click()

    def send_text(self, text):
        """
        Ecris et envoie du texte sur le chat bot.
        :param text: (str) Texte à envoyer
        """
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(text)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Send']").click()

    def click_quick_chat(self, index):
        """
        Clique sur le quick chat choisi en index.
        :param index: l'index du quick chat
        """
        self.driver.find_element_by_xpath(f"(//android.view.ViewGroup)[{index}]").click()






