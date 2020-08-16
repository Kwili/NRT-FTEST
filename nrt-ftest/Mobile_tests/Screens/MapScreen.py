class MapScreen:
    """
    Classe MapScreen.

    Recherche les différents élements de l'écran de la map à tester.
    """
    def __init__(self, driver):
        """Charge le driver."""
        self.driver = driver

    def click_allow_geo(self):
        """Clique sur autoriser la géolocalisation."""
        self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button").click()

    def click_rechercher(self):
        """Clique sur le bouton rechercher."""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Rechercher']").click()

    def click_transport(self):
        """Clique sur le bouton transport."""
        self.driver.find_element_by_class_name("android.widget.Spinner").click()

    def choose_transport(self, index):
        """Clique sur le transport choisi.
        :param index: (int) index du transport choisi.
        """
        self.driver.find_element_by_xpath(f"(//android.widget.CheckedTextView)[{index}]").click()

    def has_found_itinary(self):
        """Element apparaissant lorsqu'un itinéraire a été trouvé."""
        return self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Distance')]").click()

    def click_votre_position(self):
        """Clique sur le bouton "Votre position"."""
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'Votre')]").click()

    def write_position(self, location):
        """Ecris et envoit la position."""
        self.driver.find_element_by_xpath("//android.widget.EditText[contains(@text,'Votre')]").send_keys(location)
        self.driver.find_element_by_xpath("//android.widget.TextView[contains(@text,'3 Avenue Montaigne, Paris')]").click()

    def click_plus(self):
        """Clique sur l'element "+"."""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='+']").click()

    def click_najma(self):
        """Clique sur najma."""
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Najma']").click()

    def click_return(self):
        """Clique sur le retour."""
        self.driver.find_element_by_xpath("//android.widget.ImageView").click()






