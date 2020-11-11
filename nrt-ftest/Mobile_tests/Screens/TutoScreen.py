class TutoScreen:
    """
    Classe TutoScreen.

    Parcours les différents écrans tutoriels.
    """
    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver

    def button_click(self, text):
        """
        Ecris et envoie du texte sur le chat bot.
        :param text: (str) Texte à envoyer
        """
        self.driver.find_element_by_xpath(f"//android.widget.TextView[@text='{text}']").click()






