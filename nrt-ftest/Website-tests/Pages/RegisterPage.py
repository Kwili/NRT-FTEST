class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

        self.register_button_xpath = "//*[@id=\"root\"]/div/div/div/div/form/button[1]"
        self.already_registered_button_xpath = "//*[@id=\"root\"]/div/div/div/div/form/button[2]"

        self.error_message_xpath = "/html/body/div[3]/div/div/div[1]"
        self.error_button_xpath = "/html/body/div[3]/div/div/div[2]/button"

        self.name_textbox_id = "name-input"
        self.last_name_textbox_id = "last_name-input"
        self.birthday_textbox_id = "date-input"
        self.mail_textbox_id = "email-input"
        self.pwd_textbox_id = "password-input"
        self.confirm_pwd_textbox_id = "password-input-confirmation"
        self.person_type_id = "type-input"

    def click_register(self):
        self.driver.find_element_by_xpath(self.register_button_xpath).click()

    def click_already_registered(self):
        self.driver.find_element_by_xpath(self.already_registered_button_xpath).click()

    def click_error_button(self):
        self.driver.find_element_by_xpath(self.error_button_xpath).click()

    def check_error_message(self):
        return self.driver.find_element_by_xpath(self.error_message_xpath).text

    def enter_name(self, name):
        self.driver.find_element_by_id(self.name_textbox_id).clear()
        self.driver.find_element_by_id(self.name_textbox_id).send_keys(name)

    def enter_last_name(self, last_name):
        self.driver.find_element_by_id(self.last_name_textbox_id).clear()
        self.driver.find_element_by_id(self.last_name_textbox_id).send_keys(last_name)

    def enter_birthday(self, date):
        self.driver.find_element_by_id(self.birthday_textbox_id).clear()
        self.driver.find_element_by_id(self.birthday_textbox_id).send_keys(date)

    def enter_mail(self, mail):
        self.driver.find_element_by_id(self.mail_textbox_id).clear()
        self.driver.find_element_by_id(self.mail_textbox_id).send_keys(mail)

    def enter_pwd(self, pwd):
        self.driver.find_element_by_id(self.pwd_textbox_id).clear()
        self.driver.find_element_by_id(self.pwd_textbox_id).send_keys(pwd)

    def enter_confirm_pwd(self, pwd):
        self.driver.find_element_by_id(self.confirm_pwd_textbox_id).clear()
        self.driver.find_element_by_id(self.confirm_pwd_textbox_id).send_keys(pwd)

    def enter_person_type(self, p_type):
        self.driver.find_element_by_id(self.person_type_id).clear()
        self.driver.find_element_by_id(self.person_type_id).send_keys(p_type)

    def register(self, name, last_name, birthdate, mail, pwd, confirm_pwd, p_type):
        self.enter_name(name)
        self.enter_last_name(last_name)
        self.enter_birthday(birthdate)
        self.enter_mail(mail)
        self.enter_pwd(pwd)
        self.enter_confirm_pwd(confirm_pwd)
        self.enter_person_type(p_type)

    def check_error(self):
        message = self.check_error_message()
        self.click_error_button()
        return message
