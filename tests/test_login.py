import allure
from helpers import generate_user_data
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from test_data import REGISTER_DATA


@allure.epic("Авторизация")
class TestLogin:

    @allure.title("Успешная авторизация")
    def test_login_successful(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterPage(driver)
        login_page = LoginPage(driver)
        user_data = generate_user_data()

        main_page.open()
        main_page.click_create_account()
        register_page.register(
            first_name=REGISTER_DATA["first_name"],
            last_name=REGISTER_DATA["last_name"],
            username=user_data["username"],
            email=user_data["email"],
            password=user_data["password"]
        )

        main_page.open()
        main_page.click_login()
        login_page.login(user_data["username"], user_data["password"])

        assert "/recipes" in main_page.get_current_url()
        assert main_page.is_logout_button_displayed()