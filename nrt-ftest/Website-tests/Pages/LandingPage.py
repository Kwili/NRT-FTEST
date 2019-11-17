class LandingPage:

    def __init__(self, driver):
        self.driver = driver

        self.login_button_xpath = "//*[@id=\"root\"]/div/div/div[1]/a[1]/input"
        self.register_button_xpath = "//*[@id=\"root\"]/div/div/div[1]/a[2]/input"
        self.map_button_xpath = "//*[@id=\"root\"]/div/div/div[1]/a[3]/input"
        self.informations_button_xpath = "//*[@id=\"root\"]/div/div/div[2]/div[1]/a"
        self.image_background = "//*[@id=\"root\"]/div/div/div[2]/div[1]"
        self.image_demo = "//*[@id=\"root\"]/div/div/div[2]/div[3]/div/div[1]/img"

        self.contact_name_textbox_xpath = "//*[@id=\"ContactForm__ContactForm___HlTc\"]/form/div/div[1]/input"
        self.contact_mail_textbox_xpath = "//*[@id=\"ContactForm__ContactForm___HlTc\"]/form/div/div[2]/input"
        self.contact_object_textbox_xpath = "//*[@id=\"ContactForm__ContactForm___HlTc\"]/form/div/div[3]/input"
        self.contact_message_textbox_xpath = "//*[@id=\"ContactForm__ContactForm___HlTc\"]/form/textarea"
        self.contact_send_button_xpath = "//*[@id=\"ContactForm__ContactForm___HlTc\"]/input"

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def click_register(self):
        self.driver.find_element_by_xpath(self.register_button_xpath).click()

    def click_map(self):
        self.driver.find_element_by_xpath(self.map_button_xpath).click()

    def click_info(self):
        self.driver.find_element_by_xpath(self.informations_button_xpath).click()

    def check_image_demo(self):
        self.driver.find_element_by_xpath(self.image_demo)

    def check_image_background(self):
        self.driver.find_element_by_xpath(self.image_background)

    def check_all_images(self):
        self.check_image_background()
        self.check_image_demo()

    def contact_us(self, name, mail, mail_object, message):
        self.driver.find_element_by_xpath(self.contact_name_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.contact_name_textbox_xpath).send_keys(name)

        self.driver.find_element_by_xpath(self.contact_mail_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.contact_mail_textbox_xpath).send_keys(mail)

        self.driver.find_element_by_xpath(self.contact_object_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.contact_object_textbox_xpath).send_keys(mail_object)

        self.driver.find_element_by_xpath(self.contact_message_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.contact_message_textbox_xpath).send_keys(message)

        self.driver.find_element_by_xpath(self.contact_send_button_xpath).click()
