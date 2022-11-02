import time
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class BookPage(BasePage):
    button = (By.XPATH, "//*[contains(@class, 'button') and text() = '{0}']")
    basket = (By.XPATH, "//div[@class = 'shopping-cart-wrapper hidden-phone']")
    basket_value = (By.XPATH, "//*[@class = 'shopping-cart-wrapper mobile-cart']//span[@class = 'cart-number']")

    def __init__(self, driver):
        super(BookPage, self).__init__(driver)

    def add_to_cart(self):
        self.do_click((By.XPATH, self.button[1].format("Səbətə at")))
        time.sleep(3)
        return self.driver.find_element(*self.basket_value).get_attribute("innerText")

    def basket_hover(self):
        self.hovered(*self.basket)

    def view_shopping_cart(self):
        self.do_click((By.XPATH, "//*[@id='undefined-sticky-wrapper']//following::a[text() = 'Səbətə bax']"))

