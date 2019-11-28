from selenium.common.exceptions import NoSuchElementException


class MapPage:

    def __init__(self, driver):
        self.driver = driver

        self.research_button_xpath = "//*[@id=\"root\"]/div/div/div[1]/div[2]/div[1]/div"
        self.research_input_box_xpath = "//*[@id=\"root\"]/div/div/div[1]/div[2]/div[1]/div/form/input"
        self.reset_research_button_xpath = "//*[@id=\"root\"]/div/div/div[1]/div[2]/div[1]/div/form/a"
        self.zoom_in_button_xpath = "//*[@id=\"root\"]/div/div/div[1]/div[2]/div[3]/div/a[1]"
        self.zoom_out_button_xpath = "//*[@id=\"root\"]/div/div/div[1]/div[2]/div[3]/div/a[2]"
        self.geolocalisation_button_xpath = "//*[@id=\"root\"]/div/div/div[1]/div[2]/div[2]/div[1]/a/span"
        self.slider_button_xpath = "//*[@id=\"root\"]/div/div/div[2]/span/span[203]"
        self.slider_display_km_xpath = "//*[@id=\"discrete-slider\"]"

        self.no_itinary_founded_button_xpath = "/html/body/div[3]/div/div/div[3]/button"

    def no_ininary_founded_handler(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return
        self.driver.find_element_by_xpath(xpath).click()

    def zoom_in_and_out(self):
        self.no_ininary_founded_handler(self.no_itinary_founded_button_xpath)
        self.driver.find_element_by_xpath(self.zoom_in_button_xpath).click()
        self.driver.find_element_by_xpath(self.zoom_out_button_xpath).click()

    def geolocalisation_on_off(self):
        self.no_ininary_founded_handler(self.no_itinary_founded_button_xpath)
        self.driver.find_element_by_xpath(self.geolocalisation_button_xpath).click()
        self.driver.find_element_by_xpath(self.geolocalisation_button_xpath).click()

    def move_km_slider(self):
        self.no_ininary_founded_handler(self.no_itinary_founded_button_xpath)
        self.driver.find_element_by_xpath(self.slider_button_xpath).click()
        return self.driver.find_element_by_xpath(self.slider_display_km_xpath).text

    def research_adress(self, adress):
        self.no_ininary_founded_handler(self.no_itinary_founded_button_xpath)
        self.driver.find_element_by_xpath(self.research_button_xpath).click()
        self.driver.find_element_by_xpath(self.research_input_box_xpath).send_keys(adress)
