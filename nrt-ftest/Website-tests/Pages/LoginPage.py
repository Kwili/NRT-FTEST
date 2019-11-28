from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.mail_textbox_id = "email-input"
        self.password_textbox_id = "password-input"
        self.login_button_xpath = "//form/button[1]"
        self.register_button_xpath = "//form/button[2]"

        self.close_error_box_button_xpath = "//div[3]/div/div/div[2]/button"
        self.error_message_xpath = "//div[3]/div/div/div[1]"

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

    def check_error_message(self, error_msg):
        try:
            WebDriverWait(self.driver, 5).until(ec.text_to_be_present_in_element((By.CLASS_NAME, "modal-body"), error_msg))
        except TimeoutException:
            return self.driver.find_element_by_xpath(self.error_message_xpath).text
        return self.driver.find_element_by_xpath(self.error_message_xpath).text

    def login(self, username, pwd):
        self.enter_username(username)
        self.enter_password(pwd)
        self.click_login()

    def check_error(self, error_msg):
        message = self.check_error_message(error_msg)
        self.click_error_button()
        return message
