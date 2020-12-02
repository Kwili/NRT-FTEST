class ContactScreen:
    """
    Classe ContactScreen.

    Recherche les différents élements de l'écran contact à tester.
    """
    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver

    def click_contact_tab(self):
        """Clique sur le bouton settings."""
        self.driver.find_element_by_xpath("//android.widget.Button[contains(@content-desc,'Contact')]").click()

    def write_name(self, text):
        """Ecris le nom."""
        self.driver.find_element_by_xpath(f"//android.widget.EditText").send_keys(text)

    def write_phone(self, text):
        """
        Ecris le numéro de télephone.

        :param text:  texte à écrire.
        """
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='Mobile']").send_keys(text)

    def write_email(self, text):
        """
        Ecris l'adresse email.

        :param text:  texte à écrire.
        """
        self.driver.find_element_by_xpath("//android.widget.EditText[@text='Email']").send_keys(text)

    def write_message(self, text):
        """
        Ecris le message à envoyer.

        :param text:  texte à écrire.
        """
        self.driver.find_element_by_xpath(f"//android.widget.EditText[@text='Type your message']").send_keys(text)

    def click_submit(self):
        """Clique sur le bouton submit."""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='SUBMIT']").click()

    def click_confirm(self):
        """Clique sur le bouton confirm."""
        self.driver.find_element_by_xpath("//android.widget.Button[@text='OK']").click()




