from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_visible(self, locator):
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
        except:
            raise Exception(f"Elements with locator '{locator}' is not displayed")

    def is_clickable(self, locator):
        try:
            self.wait.until(ec.element_to_be_clickable(locator))
        except:
            raise Exception(f"Elements with locator '{locator}' is not clickable")

    def open_home_page(self, locator):
        self.driver.get("https://kitabevim.az/")
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
        except:
            raise Exception("The home page didn't open")

    def do_click(self, locator):
        self.is_clickable(locator)
        self.driver.find_element(*locator).click()

    def input_text(self, locator, text):
        self.is_clickable(locator)
        line = self.driver.find_element(*locator)
        line.click()
        line.send_keys(text + Keys.ENTER)

    def do_clear(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator)).clear()

    def get_text(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator)).text

    def hovered(self, *locator):
        element_to_hover = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element_to_hover)
        hover.perform()
