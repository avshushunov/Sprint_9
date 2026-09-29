import allure
from helpers import generate_user_data, get_asset_path
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.create_recipe_page import CreateRecipePage
from test_data import REGISTER_DATA, RECIPE_DATA


@allure.epic("Создание рецепта")
class TestCreateRecipe:

    @allure.title("Создание рецепта")
    def test_create_recipe_successful(self, driver):
        main_page = MainPage(driver)
        register_page = RegisterPage(driver)
        login_page = LoginPage(driver)
        create_recipe_page = CreateRecipePage(driver)
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

        main_page.click_create_recipe()
        create_recipe_page.fill_recipe_form(
            title=RECIPE_DATA["title"],
            description=RECIPE_DATA["description"],
            ingredient=RECIPE_DATA["ingredient"],
            image_path=get_asset_path("test_image.jpg")
        )

        assert main_page.is_recipe_card_displayed()
        assert main_page.get_recipe_title() == RECIPE_DATA["title"]