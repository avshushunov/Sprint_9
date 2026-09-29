import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from constants import URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.open_url(URL.BASE_URL)

    @allure.step("Нажать кнопку 'Создать аккаунт'")
    def click_create_account(self):
        self.click(MainPageLocators.CREATE_ACCOUNT_BUTTON)

    @allure.step("Нажать кнопку 'Войти'")
    def click_login(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Нажать кнопку 'Создать рецепт'")
    def click_create_recipe(self):
        self.click(MainPageLocators.CREATE_RECIPE_BUTTON)

    @allure.step("Проверить, что кнопка 'Выход' отображается")
    def is_logout_button_displayed(self):
        return self.is_displayed(MainPageLocators.LOGOUT_BUTTON)

    @allure.step("Проверить, что карточка рецепта отображается")
    def is_recipe_card_displayed(self):
        self.wait_for_element(MainPageLocators.RECIPE_CARD)
        return self.is_displayed(MainPageLocators.RECIPE_CARD)

    @allure.step("Получить заголовок рецепта")
    def get_recipe_title(self):
        self.wait_for_element_has_text(MainPageLocators.RECIPE_TITLE)
        return self.get_text(MainPageLocators.RECIPE_TITLE)