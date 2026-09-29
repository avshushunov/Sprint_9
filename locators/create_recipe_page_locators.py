from selenium.webdriver.common.by import By


class CreateRecipePageLocators:
    TITLE_INPUT = (By.XPATH, "//div[text()='Название рецепта']/following-sibling::input")
    COOKING_TIME_INPUT = (By.XPATH, "//div[text()='Время приготовления']/following-sibling::input")
    DESCRIPTION_INPUT = (By.XPATH, "//div[text()='Описание рецепта']/following-sibling::textarea")
    INGREDIENT_INPUT = (By.XPATH, "//div[text()='Ингредиенты']/following-sibling::input")
    INGREDIENT_AMOUNT_INPUT = (By.XPATH, "//div[contains(@class, 'ingredientsAmountInput')]//input")
    INGREDIENT_ADD_BUTTON = (By.XPATH, "//div[text()='Добавить ингредиент']")
    IMAGE_INPUT = (By.XPATH, "//label[text()='Загрузить фото']/following-sibling::input")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Создать рецепт']")
    INGREDIENT_SUGGESTION = "//div[text()='{}']"