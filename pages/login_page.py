import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    @allure.step("Авторизоваться")
    def login(self, username, password):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, username)
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_url_change("signin")

    @allure.step("Проверить, что форма авторизации отображается")
    def is_login_form_displayed(self):
        return self.is_displayed(LoginPageLocators.LOGIN_FORM)