import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        self.find_element(locator).click()

    @allure.step("Ввести '{text}' в поле {locator}")
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверить, что элемент {locator} отображается")
    def is_displayed(self, locator):
        return self.find_element(locator).is_displayed()

    @allure.step("Ожидать появления элемента {locator}")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидать кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидать что элемент {locator} станет активным")
    def wait_for_element_enabled(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).is_enabled()
        )

    @allure.step("Ожидать что текст элемента {locator} не пустой")
    def wait_for_element_has_text(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: d.find_element(*locator).text != ""
        )

    @allure.step("Ожидать ухода со страницы содержащей '{keyword}' в URL")
    def wait_for_url_change(self, keyword, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: keyword not in d.current_url
        )

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url