class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.mail_textbox_id = "email-input"
        self.password_textbox_id = "password-input"
        self.login_button_xpath = "//*[@id=\"root\"]/div/div/div/form/button[1]"
        self.register_button_xpath = "//*[@id=\"root\"]/div/div/div/form/button[2]"

        self.close_error_box_button_xpath = "/html/body/div[3]/div/div/div[2]/button"
        self.error_message_xpath = "/html/body/div[3]/div/div/div[1]"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.mail_textbox_id).clear()
        self.driver.find_element_by_id(self.mail_textbox_id).send_keys(username)

    def enter_password(self, pwd):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(pwd)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def click_register(self):
        self.driver.find_element_by_xpath(self.register_button_xpath).click()

    def click_error_button(self):
        self.driver.find_element_by_xpath(self.close_error_box_button_xpath).click()

    def check_error_message(self):
        return self.driver.find_element_by_xpath(self.error_message_xpath).text

    def login(self, username, pwd):
        self.enter_username(username)
        self.enter_password(pwd)
        self.click_login()

    def check_error(self):
        message = self.check_error_message()
        self.click_error_button()
        return message
