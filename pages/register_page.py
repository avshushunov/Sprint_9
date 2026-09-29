import allure
from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators


class RegisterPage(BasePage):

    @allure.step("Заполнить форму регистрации")
    def register(self, first_name, last_name, username, email, password):
        self.send_keys(RegisterPageLocators.FIRST_NAME_INPUT, first_name)
        self.send_keys(RegisterPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(RegisterPageLocators.USERNAME_INPUT, username)
        self.send_keys(RegisterPageLocators.EMAIL_INPUT, email)
        self.send_keys(RegisterPageLocators.PASSWORD_INPUT, password)
        self.click(RegisterPageLocators.SUBMIT_BUTTON)
        self.wait_for_url_change("signup")