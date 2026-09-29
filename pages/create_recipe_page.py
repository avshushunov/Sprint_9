import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.create_recipe_page_locators import CreateRecipePageLocators


class CreateRecipePage(BasePage):

    @allure.step("Заполнить форму создания рецепта: '{title}'")
    def fill_recipe_form(self, title, description, ingredient, image_path):
        self.send_keys(CreateRecipePageLocators.TITLE_INPUT, title)
        self.send_keys(CreateRecipePageLocators.COOKING_TIME_INPUT, "30")
        self.send_keys(CreateRecipePageLocators.DESCRIPTION_INPUT, description)
        self.add_ingredient(ingredient)
        self.send_keys(CreateRecipePageLocators.IMAGE_INPUT, image_path)
        self.wait_for_element_enabled(CreateRecipePageLocators.SUBMIT_BUTTON)
        self.click(CreateRecipePageLocators.SUBMIT_BUTTON)
        self.wait_for_url_change("create")

    @allure.step("Добавить ингредиент: '{ingredient}'")
    def add_ingredient(self, ingredient):
        self.send_keys(CreateRecipePageLocators.INGREDIENT_INPUT, ingredient)
        suggestion = (By.XPATH, CreateRecipePageLocators.INGREDIENT_SUGGESTION.format(ingredient))
        self.wait_for_element(suggestion)
        self.click(suggestion)
        self.send_keys(CreateRecipePageLocators.INGREDIENT_AMOUNT_INPUT, "100")
        self.wait_for_element_clickable(CreateRecipePageLocators.INGREDIENT_ADD_BUTTON)
        self.click(CreateRecipePageLocators.INGREDIENT_ADD_BUTTON)