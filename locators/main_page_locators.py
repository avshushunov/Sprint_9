from selenium.webdriver.common.by import By


class MainPageLocators:
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//a[text()='Создать аккаунт']")
    LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Выход']")
    CREATE_RECIPE_BUTTON = (By.XPATH, "//a[text()='Создать рецепт']")
    RECIPE_CARD = (By.XPATH, "//div[contains(@class, 'single-card')]")
    RECIPE_TITLE = (By.XPATH, "//h1[contains(@class, 'single-card__title')]")