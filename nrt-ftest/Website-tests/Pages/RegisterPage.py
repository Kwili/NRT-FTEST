from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

        self.register_button_xpath = "//form/button[1]"
        self.already_registered_button_xpath = "//form/button[2]"

        self.error_message_xpath = "//div[3]/div/div/div[1]"
        self.error_button_xpath = "//div[3]/div/div/div[2]/button"

    def click_register(self):
        self.driver.find_element_by_xpath(self.register_button_xpath).click()

    def click_already_registered(self):
        self.driver.find_element_by_xpath(self.already_registered_button_xpath).click()

    def click_error_button(self):
        self.driver.find_element_by_xpath(self.error_button_xpath).click()

    def enter_name(self, name):
        self.driver.find_element_by_xpath("//input[@field='name']").clear()
        self.driver.find_element_by_xpath("//input[@field='name']").send_keys(name)

    def enter_last_name(self, last_name):
        self.driver.find_element_by_xpath("//input[@field='last_name']").clear()
        self.driver.find_element_by_xpath("//input[@field='last_name']").send_keys(last_name)

    def enter_birthday(self, date):
        self.driver.find_element_by_xpath("//input[@type='date']").clear()
        self.driver.find_element_by_xpath("//input[@type='date']").send_keys(date)

    def enter_mail(self, mail):
        self.driver.find_element_by_xpath("//input[@type='email']").clear()
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys(mail)

    def enter_pwd(self, pwd):
        self.driver.find_element_by_xpath("//input[@placeholder='Mot de passe']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Mot de passe']").send_keys(pwd)

    def enter_confirm_pwd(self, pwd):
        self.driver.find_element_by_xpath("//input[@placeholder='Confirmation du mot de passe']").clear()
        self.driver.find_element_by_xpath("//input[@placeholder='Confirmation du mot de passe']").send_keys(pwd)

    def register(self, name, last_name, birthdate, mail, pwd, confirm_pwd, p_type):
        self.enter_name(name)
        self.enter_last_name(last_name)
        self.enter_birthday(birthdate)
        self.enter_mail(mail)
        self.enter_pwd(pwd)
        self.enter_confirm_pwd(confirm_pwd)

    def check_error_message(self, error_msg):
        try:
            WebDriverWait(self.driver, 5).until(ec.text_to_be_present_in_element((By.XPATH, self.error_message_xpath), error_msg))
        except TimeoutException:
            return self.driver.find_element_by_xpath(self.error_message_xpath).text
        return self.driver.find_element_by_xpath(self.error_message_xpath).text

    def check_error(self, error_msg):
        message = self.check_error_message(error_msg)
        self.click_error_button()
        return message
