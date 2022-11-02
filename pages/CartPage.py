import time
from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CartPage(BasePage):
    plus = (By.XPATH, "//*[@id='post-52']//input[@value='+']")
    button_reload_cart = (By.XPATH, "//button[contains(text(),'Səbəti yenilə')]")
    reload_message = (By.XPATH, "//div[contains(text(),'Səbət yeniləndi')]")
    button_cross = (By.XPATH, "//td[@class = 'product-remove']")
    empty_basket = (By.XPATH, "//*[contains(text(),'Səbətiniz hazırda boşdur.')]")

    def __init__(self, driver):
        super(CartPage, self).__init__(driver)

    def increase_by_one(self):
        self.do_click(self.plus)

    def reload_cart(self):
        self.do_click(self.button_reload_cart)
        self.is_visible(self.reload_message)
        return self.driver.find_element(By.XPATH, "//div[@class = 'woocommerce-message']").text

    def click_cross(self):
        self.do_click(self.button_cross)

    def check_basket(self):
        self.is_visible((By.XPATH, "//*[@class='cart-empty woocommerce-info']"))
        return self.driver.find_element(By.XPATH, "//*[@class='cart-empty woocommerce-info']").text

